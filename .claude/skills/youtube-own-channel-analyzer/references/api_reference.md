# YouTube Data API v3 Reference

## Authentication

All requests require `key={API_KEY}` parameter.

Get API key: [Google Cloud Console](https://console.cloud.google.com/apis/credentials)
1. Create project → Enable YouTube Data API v3 → Create credentials → API Key

## Channels Endpoint

```
GET https://www.googleapis.com/youtube/v3/channels
```

### Parameters
| Param | Required | Description |
|-------|----------|-------------|
| part | Yes | snippet,statistics,contentDetails,brandingSettings |
| id | One of | Channel ID (UC...) |
| forUsername | One of | Legacy username |
| key | Yes | API key |

### Response Fields
```json
{
  "items": [{
    "id": "UC...",
    "snippet": {
      "title": "Channel Name",
      "description": "...",
      "customUrl": "@handle",
      "publishedAt": "2020-01-01T00:00:00Z",
      "country": "US",
      "thumbnails": { "default": {}, "medium": {}, "high": {} }
    },
    "statistics": {
      "viewCount": "1000000",
      "subscriberCount": "50000",
      "hiddenSubscriberCount": false,
      "videoCount": "200"
    },
    "contentDetails": {
      "relatedPlaylists": {
        "uploads": "UU..."
      }
    },
    "brandingSettings": {
      "channel": {
        "keywords": "keyword1 keyword2"
      }
    }
  }]
}
```

## Search Endpoint

```
GET https://www.googleapis.com/youtube/v3/search
```

### Parameters
| Param | Required | Description |
|-------|----------|-------------|
| part | Yes | snippet |
| channelId | No | Filter by channel |
| q | No | Search query |
| type | No | video, channel, playlist |
| order | No | date, rating, relevance, viewCount |
| maxResults | No | 1-50 (default 5) |
| pageToken | No | For pagination |
| key | Yes | API key |

### Response
```json
{
  "nextPageToken": "...",
  "prevPageToken": "...",
  "pageInfo": { "totalResults": 100, "resultsPerPage": 50 },
  "items": [{
    "id": {
      "kind": "youtube#video",
      "videoId": "..."
    },
    "snippet": {
      "publishedAt": "...",
      "channelId": "...",
      "title": "...",
      "description": "...",
      "thumbnails": {}
    }
  }]
}
```

## Videos Endpoint

```
GET https://www.googleapis.com/youtube/v3/videos
```

### Parameters
| Param | Required | Description |
|-------|----------|-------------|
| part | Yes | snippet,statistics,contentDetails |
| id | Yes | Comma-separated video IDs (max 50) |
| key | Yes | API key |

### Response Fields
```json
{
  "items": [{
    "id": "videoId",
    "snippet": {
      "publishedAt": "...",
      "channelId": "...",
      "title": "...",
      "description": "...",
      "tags": ["tag1", "tag2"],
      "categoryId": "22"
    },
    "statistics": {
      "viewCount": "10000",
      "likeCount": "500",
      "commentCount": "50"
    },
    "contentDetails": {
      "duration": "PT10M30S",
      "definition": "hd"
    }
  }]
}
```

## PlaylistItems Endpoint

```
GET https://www.googleapis.com/youtube/v3/playlistItems
```

### Parameters
| Param | Required | Description |
|-------|----------|-------------|
| part | Yes | snippet,contentDetails |
| playlistId | Yes | Playlist ID (uploads: UU...) |
| maxResults | No | 1-50 |
| pageToken | No | For pagination |
| key | Yes | API key |

## Quota Costs

| Operation | Cost |
|-----------|------|
| search.list | 100 |
| channels.list | 1 |
| videos.list | 1 |
| playlistItems.list | 1 |

**Daily quota**: 10,000 units (default)

## Error Codes

| Code | Meaning |
|------|---------|
| 400 | Bad request (invalid params) |
| 403 | Forbidden (quota exceeded, API not enabled) |
| 404 | Not found |
| 429 | Too many requests |

## Duration Format (ISO 8601)

Format: `PT{hours}H{minutes}M{seconds}S`

Examples:
- `PT1H30M` = 1 hour 30 minutes
- `PT10M30S` = 10 minutes 30 seconds
- `PT45S` = 45 seconds

Parse with regex: `/PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?/`
