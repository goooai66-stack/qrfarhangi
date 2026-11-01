/**
 * Google Apps Script web app for qrfarhangi.
 * Serves index.html as a web page (Deploy > New deployment > Web app).
 */
function doGet() {
  return HtmlService.createHtmlOutputFromFile('index')
    .setTitle('اطلاعات حساب بانکی')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1.0')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}
