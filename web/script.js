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

    // очистка div с тегом result
    document.getElementById("result").innerHTML = "";


    var table = document.getElementById("myTable");
    var rowCount = table.rows.length;
    var columnCount = table.rows[0].cells.length;

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

    //вывод результата
    var resultBlock = document.getElementById("result");
    resultBlock.style.display = "block";
    resultBlock.style.opacity = 0;

    // Используем requestAnimationFrame для анимации
    var opacity = 0;
    var animation = function (currentTime) {
        opacity += 0.01; // изменение значения opacity (можно настроить скорость)
        resultBlock.style.opacity = opacity;

        if (opacity < 1) {
            requestAnimationFrame(animation);
        }
    };

    requestAnimationFrame(animation);


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

    }

    eel.get_result()(function (get_result) {
        var table = "<table class='table'>";
        table += "<thead><tr><th scope='col'>Номер критерия</th>";
        for (let i = 0; i < (get_result[0].length / 2); i++) {
            table += "<th scope='col'>Значение</th>";
        }
        table += "</tr></thead>";
        table += "<tbody>";

        for (i = 0; i < get_result.length; i++) {
            table += "<tr>";
            table += "<th scope='row' rowspan='2'>K" + (i + 1) + "</th>";

            if (get_result[0].length > 2) {

                for (var k = 0; k < get_result[i].length; k = k + 2) {
                    table += "<td>" + get_result[i][k] + "</td>";
                }
                table += "</tr><tr>"

                for (var k = 1; k < get_result[i].length; k = k + 2) {
                    table += "<td>" + get_result[i][k] + "</td>";
                }
                table += "</tr>"
            } else {
                table += "<td>" + get_result[i][0] + "</td>";
                table += "</tr>";
                table += "<tr>";
                table += "<td>" + get_result[i][1] + "</td>";
                table += "</tr>";

            }
        }
        table += "</tbody></table>";
        document.getElementById("result").innerHTML = table;
        eel.clear()();
    });
}

function addNewColumn() {
    var table = document.getElementById("myTable");
    var rowCount = table.rows.length;

    for (var i = 0; i < rowCount; i++) {
        var row = table.rows[i];
        var cellId = "row" + (i + 1) + "col" + columnIndex;

        for (var j = 0; j < 2; j++) {
            var cell = row.insertCell(-1);
            var input = document.createElement("input");
            input.type = "text";
            input.className = "form-control";
            input.id = cellId;
            cell.appendChild(input);
            columnIndex++;
        }
    }
}

function removeTwoColumns() {
        // Reload the page after removing columns
        location.reload();
}

 eel.expose(updateDropdown);

      function updateDropdown(alloys) {
    var dropdownMenu = document.getElementById('dropdown-menu');
    var selectedItemInput = document.getElementById('selectedItem');

    // Очистите текущие элементы в выпадающем списке
    dropdownMenu.innerHTML = '';

    // Добавьте новые элементы в выпадающий список
    alloys.forEach(function (alloy) {
        var listItem = document.createElement('li');
        var link = document.createElement('a');
        link.className = 'dropdown-item';
        link.href = '#';
        link.textContent = alloy;

        // Добавляем обработчик события клика на каждый элемент списка
        link.addEventListener('click', function () {
            selectedItemInput.value = alloy;
        });

        listItem.appendChild(link);
        dropdownMenu.appendChild(listItem);
    });
}

// Вызывайте функцию dropdown из Python, когда страница загружена
window.onload = function () {
    eel.dropdown()(updateDropdown);
};
