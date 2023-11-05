var columnIndex = 4;
var cValues = [];
var lambdaValues = [];
var roValues = [];
var alphaValues = [];
var eValues = [];
var hrcValues = [];
var sigmaValues = [];
var sigmaValues2 = [];
var kcuValues = [];
var deltaValues = [];
var psiValues = [];
var muValues = [];
var tauValues = [];
var tkValues = [];
var tfValues = [];


function getSquare() {
    var number = document.getElementById("number").value;
    eel.get_square_result(number)(function (result) {
        document.getElementById("result").innerText = "Result: " + result;
    });
}


function calculate() {
    cValues = [];
    lambdaValues = [];
    roValues = [];
    alphaValues = [];
    eValues = [];
    hrcValues = [];
    sigmaValues = [];
    sigmaValues2 = [];
    kcuValues = [];
    deltaValues = [];
    psiValues = [];
    muValues = [];
    tauValues = [];
    tkValues = [];
    tfValues = [];

    var table = document.getElementById("myTable");
    var rowCount = table.rows.length;
    var columnCount = table.rows[0].cells.length;
    console.log(rowCount)
    console.log(columnCount)
    console.log("------")

    for (var i = 0; i < rowCount; i++) {
        for (var c = 2; c <= columnCount; c++) {
            // вывод значения ячейки
            var cellId = "row" + (i + 1) + "col" + c;
            var cellValue = document.getElementById(cellId).value;
            if (i == 0) {
                cValues.push(cellValue);
            } else if (i == 1) {
                lambdaValues.push(cellValue);
            } else if (i == 2) {
                roValues.push(cellValue);
            } else if (i == 3) {
                alphaValues.push(cellValue);
            } else if (i == 4) {
                eValues.push(cellValue);
            } else if (i == 5) {
                hrcValues.push(cellValue);
            } else if (i == 6) {
                sigmaValues.push(cellValue);
            } else if (i == 7) {
                sigmaValues2.push(cellValue);
            } else if (i == 8) {
                kcuValues.push(cellValue);
            } else if (i == 9) {
                deltaValues.push(cellValue);
            } else if (i == 10) {
                psiValues.push(cellValue);
            } else if (i == 11) {
                muValues.push(cellValue);
            } else if (i == 12) {
                tauValues.push(cellValue);
            } else if (i == 13) {
                tkValues.push(cellValue);
            } else if (i == 14) {
                tfValues.push(cellValue);
            }

        }
    }


    //cкрытие таблицы
    document.getElementById("myTable").style.display = "none";

    //вывод результата
    document.getElementById("result").style.display = "block";

    console.log(cValues.length)

    for (var i = 0; i < cValues.length; i++) {
        var cValue = cValues[i];
        var lambdaValue = lambdaValues[i];
        var roValue = roValues[i];
        var alphaValue = alphaValues[i];
        var eValue = eValues[i];
        var hrcValue = hrcValues[i];
        var sigmaValue = sigmaValues[i];
        var sigmaValue2 = sigmaValues2[i];
        var kcuValue = kcuValues[i];
        var deltaValue = deltaValues[i];
        var psiValue = psiValues[i];
        var muValue = muValues[i];
        var tauValue = tauValues[i];
        var tkValue = tkValues[i];
        var tfValue = tfValues[i];

        eel.add_to_array(cValue, lambdaValue, roValue, alphaValue, eValue, hrcValue, sigmaValue, sigmaValue2, kcuValue, deltaValue, psiValue, muValue, tauValue, tkValue, tfValue)(function (K1_values, K2_values, K3_values, K4_values, K5_values, K6_values, K7_values, K8_values, K9_values, K10_values, K11_values, K12_values, K13_values, K14_values, K15_values, K16_values) {
            document.getElementById("result").innerText = "Result: " + K1_values + " " + K2_values + " " + K3_values + " " + K4_values + " " + K5_values + " " + K6_values + " " + K7_values + " " + K8_values + " " + K9_values + " " + K10_values + " " + K11_values + " " + K12_values + " " + K13_values + " " + K14_values + " " + K15_values + " " + K16_values;
        });
    }

    // console.log(value)
    // eel.get_square_result(value)(function (result) {
    //     document.getElementById("result").innerText = "Result: " + result;
    // });

}

function addNewColumn() {
    var table = document.getElementById("myTable");
    var rowCount = table.rows.length;

    for (var i = 0; i < rowCount; i++) {
        var cell = table.rows[i].insertCell(-1);
        var rowId = i + 1;
        var cellId = "row" + rowId + "col" + columnIndex;
        cell.innerHTML = "<input type='text' class='form-control' id='" + cellId + "'>";
    }
    columnIndex++;
}
