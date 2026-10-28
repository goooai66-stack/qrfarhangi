#!/usr/bin/env python3
"""Build the claude.ai Project bundle from plugins/ruqyah-youtube.

    python3 tools/build_claude_project.py

Writes claude-project/:
  skills/<name>.zip   one zip per skill, for Settings > Capabilities > Skills on claude.ai
  knowledge/          niche.md and voice.md, for the Project's knowledge
  instructions.md     is hand-written and left alone

Each zipped skill is standalone: it carries its own channel/niche.md and channel/voice.md, and the
files it otherwise reads from a sibling skill folder (hooks.json, deadair.py).
"""
import os, re, shutil, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGIN = os.path.join(ROOT, "plugins", "ruqyah-youtube")
SKILLS = os.path.join(PLUGIN, "skills")
CHANNEL = os.path.join(PLUGIN, "youtube")
OUT = os.path.join(ROOT, "claude-project")

# files a skill reads from a sibling folder, copied in so the zip works on its own
EXTRA = {
    "yt-viral": [("yt-script", "hooks.json")],
    "yt-chapters": [("yt-edit", "deadair.py")],
    "yt-retention": [("yt-edit", "deadair.py")],
}


def skill_md(text):
    # the plugin points at ../../youtube/; a standalone zip carries the files under channel/
    text = text.replace("../../youtube/", "channel/")
    return text.replace("the plugin's copy", "this skill's copy").replace(
        "the plugin's template", "this skill's template")


def build_zip(name):
    src = os.path.join(SKILLS, name)
    dest = os.path.join(OUT, "skills", name + ".zip")
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
        for base, dirs, files in os.walk(src):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in sorted(files):
                path = os.path.join(base, f)
                arc = os.path.join(name, os.path.relpath(path, src))
                if f == "SKILL.md" and base == src:
                    z.writestr(arc, skill_md(open(path, encoding="utf-8").read()))
                else:
                    z.write(path, arc)
        for sibling, f in EXTRA.get(name, []):
            z.write(os.path.join(SKILLS, sibling, f), os.path.join(name, f))
        for f in ("niche.md", "voice.md"):
            z.write(os.path.join(CHANNEL, f), os.path.join(name, "channel", f))
    return dest


def main():
    for sub in ("skills", "knowledge"):
        shutil.rmtree(os.path.join(OUT, sub), ignore_errors=True)
        os.makedirs(os.path.join(OUT, sub))
    names = sorted(d for d in os.listdir(SKILLS) if os.path.isfile(os.path.join(SKILLS, d, "SKILL.md")))
    for n in names:
        print("  zip ", os.path.relpath(build_zip(n), ROOT))
    for f in ("niche.md", "voice.md"):
        text = open(os.path.join(CHANNEL, f), encoding="utf-8").read()
        # the knowledge copy has no skills folder next to it
        text = re.sub(r"\[([^\]]+)\]\(\.\./skills/[^)]+\)", r"\1", text)
        open(os.path.join(OUT, "knowledge", f), "w", encoding="utf-8").write(text)
        print("  copy", os.path.join("claude-project", "knowledge", f))
    print(f"\n  {len(names)} skills")


if __name__ == "__main__":
    main()
