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
            switch (i) {
                case 0:
                    cValues.push(cellValue);
                    break;
                case 1:
                    lambdaValues.push(cellValue);
                    break;
                case 2:
                    roValues.push(cellValue);
                    break;
                case 3:
                    alphaValues.push(cellValue);
                    break;
                case 4:
                    eValues.push(cellValue);
                    break;
                case 5:
                    hrcValues.push(cellValue);
                    break;
                case 6:
                    sigmaValues.push(cellValue);
                    break;
                case 7:
                    sigmaValues2.push(cellValue);
                    break;
                case 8:
                    kcuValues.push(cellValue);
                    break;
                case 9:
                    deltaValues.push(cellValue);
                    break;
                case 10:
                    psiValues.push(cellValue);
                    break;
                case 11:
                    muValues.push(cellValue);
                    break;
                case 12:
                    tauValues.push(cellValue);
                    break;
                case 13:
                    tkValues.push(cellValue);
                    break;
                case 14:
                    tfValues.push(cellValue);
                    break;
                default:
                    break;
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
        });

        console.log("Цикл выполнися " + i + " раз")
    }

    eel.get_result()(function (get_result) {
        var table = "<table class='table table-bordered'>";
        for (var i = 0; i < get_result.length; i++) {
            table += "<tr>";
            for (var j = 0; j < get_result[i].length; j++) {
                table += "<td>K" + (i + 1) + (j !== 0 ? "." + (j + 1) : "") + " = " + get_result[i][j].toFixed(4) + "</td>";
            }
            table += "</tr>";
        }
        table += "</table>";
        document.getElementById("result").innerHTML = table;
    });


    // eel.get_result()(function (get_result) {
    //
    //
    //         var K1 = get_result[0];
    //         var K2 = get_result[1];
    //         var K3 = get_result[2];
    //         var K4 = get_result[3];
    //         var K5 = get_result[4];
    //         var K6 = get_result[5];
    //         var K7 = get_result[6];
    //         var K8 = get_result[7];
    //         var K9 = get_result[8];
    //         var K10 = get_result[9];
    //         var K11 = get_result[10];
    //         var K12 = get_result[11];
    //         var K13 = get_result[12];
    //         var K14 = get_result[13];
    //         var K15 = get_result[14];
    //         var K16 = get_result[15];
    //
    //
    //         var result_text = "K1 = " + K1 + "\n" + "K2 = " + K2 + "\n" + "K3 = " + K3 + "\n" + "K4 = " + K4 + "\n" + "K5 = " + K5 + "\n" + "K6 = " + K6 + "\n" + "K7 = " + K7 + "\n" + "K8 = " + K8 + "\n" + "K9 = " + K9 + "\n" + "K10 = " + K10 + "\n" + "K11 = " + K11 + "\n" + "K12 = " + K12 + "\n" + "K13 = " + K13 + "\n" + "K14 = " + K14 + "\n" + "K15 = " + K15 + "\n" + "K16 = " + K16 + "\n";
    //         document.getElementById("result").innerText = result_text;
    //
    //
    //     }
    // );

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
    for (var i = 0; i < rowCount; i++) {
        var cell = table.rows[i].insertCell(-1);
        var rowId = i + 1;
        var cellId = "row" + rowId + "col" + columnIndex;
        cell.innerHTML = "<input type='text' class='form-control' id='" + cellId + "'>";
    }
    columnIndex++;
}
