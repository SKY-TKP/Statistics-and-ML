function onEdit(e) {
  var sheet = e.range.getSheet();
  var sheetName = sheet.getName();
  var row = e.range.getRow();
  var col = e.range.getColumn();
  var value = e.value;

  var sheetConfig = {
    "Day1": { inputCol: 20, changeCols: [17, 18, 19], noteCol: 20 }, // T, Q, R, S, Note in T
    "Day2": { inputCol: 18, changeCols: [15, 16, 17], noteCol: 18 }, // R, O, P, Q, Note in R
    "Day3": { inputCol: 16, changeCols: [13, 14, 15], noteCol: 16 }, // P, M, N, O, Note in P
    "Day4": { inputCol: 16, changeCols: [13, 14, 15], noteCol: 16 }  // P, M, N, O, Note in P
  };

  var sheetNames = Object.keys(sheetConfig);

  if (sheetConfig[sheetName] && (value && (value.toString().includes("สละสิทธิ์") || value.toString().includes("reset")))) { // ตรวจสอบทั้ง "สละสิทธิ์" และ "reset"
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var currentSheetIndex = sheetNames.indexOf(sheetName);
    var setValue = value.toString().includes("สละสิทธิ์") ? true : false; // กำหนดค่าที่จะตั้ง (true หรือ false)

    // ทำให้ Day ปัจจุบันเป็น True/False ก่อน
    var currentConfig = sheetConfig[sheetName];
    for (var j = 0; j < currentConfig.changeCols.length; j++) {
      sheet.getRange(row, currentConfig.changeCols[j]).setValue(setValue);
    }

    // วนลูปชีตถัดไป
    for (var i = currentSheetIndex + 1; i < sheetNames.length; i++) {
      var targetSheetName = sheetNames[i];
      var targetSheet = ss.getSheetByName(targetSheetName);

      if (targetSheet && sheetConfig[targetSheetName]) {
        var targetConfig = sheetConfig[targetSheetName];

        for (var j = 0; j < targetConfig.changeCols.length; j++) {
          targetSheet.getRange(row, targetConfig.changeCols[j]).setValue(setValue);
        }

        targetSheet.getRange(row, targetConfig.noteCol).setValue(value.toString().includes("สละสิทธิ์") ? "สละสิทธิ์" : ""); // เขียน "สละสิทธิ์" หรือล้างค่า
      }
    }
  }
}
