var columnIndex = 6;
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

    for (var i = 0; i < rowCount - 1; i++) {
        for (var c = 2; c <= columnCount; c++) {
            // вывод значения ячейки
            var cellId = "row" + (i + 1) + "col" + c;
            var cellValue = document.getElementById(cellId);
            if (cellValue) {
                cellValue = cellValue.value;
            }

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
        for (let i = 0; i <= (get_result.length / 2); i++) {
            table += "<th scope='col'>Значение</th>";
        }
        table += "</tr></thead>";
        table += "<tbody>";

        for (i = 0; i < get_result[0].length; i++) {
            table += "<tr>";
            table += "<th scope='row' rowspan='2'>K" + (i + 1) + "</th>";

            if (get_result[0][0].length > 2) {
                for (var k = 0; k < get_result[0][i].length; k++) {
                    // console.log(get_result[0][i].length);
                    console.log('get_result[0][i][k]:', get_result[0][i][k]); // вывод значения ячейки
                    console.log('k', k);
                    console.log('k%2', k % 2);
                    table += "<td>" + get_result[0][i][k] + "</td>";

                    // Если k четное, добавить закрывающий тег </tr> и открыть новую строку <tr>
                    if (k % 2 === 1) {
                        table += "</tr><tr>";
                    }
                }

            }
            table = table.slice(0, -9);
            // Добавление столбца рангов
            table += "<td rowspan='2'>" + get_result[1][i][1] + "</td>";
            table += "<td rowspan='2'>" + get_result[1][i][2] + "</td>";

            table += "</tr>";
        }
        table += "</tbody></table>";
        document.getElementById("result").innerHTML = table;
        eel.clear()();
    });
}

function addNewColumn() {
    var table = document.getElementById("myTable");
    var rowCount = table.rows.length;

    // Add two header cells (<th>) with the specified structure
    for (var k = 0; k < 2; k++) {
        var headerCell = document.createElement("th");
        var inputGroup = document.createElement("div");
        inputGroup.className = "input-group mb-3";

        var input = document.createElement("input");
        input.id = "selectedItem" + (columnIndex - 1);
        input.className = "form-control text-right";
        input.setAttribute("aria-label", "Text input with dropdown button");
        input.placeholder = "Сплав " + (columnIndex - 1);

        var button = document.createElement("button");
        button.className = "btn btn-outline-secondary dropdown-toggle";
        button.type = "button";
        button.setAttribute("data-bs-toggle", "dropdown");
        button.setAttribute("aria-expanded", "false");

        var ul = document.createElement("ul");
        ul.className = "dropdown-menu dropdown-menu-end";
        ul.id = "dropdown-menu" + (columnIndex - 1);

        inputGroup.appendChild(input);
        inputGroup.appendChild(button);
        inputGroup.appendChild(ul);
        headerCell.appendChild(inputGroup);
        table.rows[0].appendChild(headerCell);
        columnIndex++;
    }
    for (var i = 0; i < rowCount - 1; i++) {
        var row = table.rows[i + 1];
        if (!row) {
            row = table.insertRow(i + 1);
        }

        for (var j = 0; j < 2; j++) {
            var cell = row.insertCell(-1);
            var input = document.createElement("input");
            input.type = "number";
            input.min = "0";
            input.className = "form-control text-right";
            input.id = "row" + (i + 1) + "col" + (columnIndex - 2 + j);
            cell.appendChild(input);

            initializeDropdown('selectedItem' + (columnIndex - 3 + j), 'dropdown-menu' + (columnIndex - 3 + j));
        }
    }
}


function removeTwoColumns() {
    // Reload the page after removing columns
    location.reload();
}


// eel.expose(updateDropdown);
function initializeDropdown(buttonId, menuId) {
    var button = document.getElementById(buttonId);
    var dropdownMenu = document.getElementById(menuId);
    var selectedItemInput = document.getElementById('selectedItem' + buttonId.slice(-1));

    eel.dropdown()(function (alloys) {
        // Clear the current items in the dropdown menu
        try {
            var dropdownItems = dropdownMenu.querySelectorAll('li');
            dropdownItems.forEach(function (item) {
                item.remove();
            });
        } catch (e) {
            console.log(e);
        }
        // Add new items to the dropdown menu
        alloys.forEach(function (alloy) {
            var listItem = document.createElement('li');
            var link = document.createElement('a');
            link.className = 'dropdown-item';
            link.href = '#';
            link.textContent = alloy;

            // Add a click event listener to each dropdown item
            link.addEventListener('click', function () {
                selectedItemInput.value = alloy;
                console.log('Значение изменилось:', selectedItemInput.value);
                eel.dropdown_select(selectedItemInput.value)(function (result) {


                    var table = document.getElementById("myTable");
                    var rowCount = table.rows.length;

                    for (var i = 0; i < rowCount - 1; i++) {
                        // вывод значения ячейки
                        var cellId = "row" + (i + 1) + "col" + (parseInt(buttonId.slice(-1)) + 1);
                        var cellValue = document.getElementById(cellId);
                        if (cellValue) {
                            cellValue.value = result[i];
                        }

                    }
                });
            })

            listItem.appendChild(link);
            dropdownMenu.appendChild(listItem);
        });
    });

    // Add an event listener to the button to toggle the dropdown menu
    button.addEventListener('click', function () {
        dropdownMenu.classList.toggle('show');
    });

    // Close the dropdown menu if the user clicks outside of it
    window.addEventListener('click', function (event) {
        if (!event.target.matches('.dropdown-toggle')) {
            var dropdowns = document.getElementsByClassName('dropdown-menu');
            for (var i = 0; i < dropdowns.length; i++) {
                var openDropdown = dropdowns[i];
                if (openDropdown.classList.contains('show')) {
                    openDropdown.classList.remove('show');
                }
            }
        }
    });
}

// Call the initializeDropdown function for each set of button and menu
window.onload = function () {
    initializeDropdown('selectedItem1', 'dropdown-menu1');
    initializeDropdown('selectedItem2', 'dropdown-menu2');
    initializeDropdown('selectedItem3', 'dropdown-menu3');
    initializeDropdown('selectedItem4', 'dropdown-menu4');

};


// Функция для парсинга данных из HTML
function parseData() {
    const labels = [];
    const values1 = [];
    const values2 = [];

    const rows = document.querySelectorAll('tbody tr');
    let currentLabel = '';

    rows.forEach((row, index) => {
        const cells = row.querySelectorAll('th, td');
        if (cells.length === 1) {
            currentLabel = cells[0].textContent.trim();
        } else {
            labels.push(currentLabel);
            values1.push(parseFloat(cells[0].textContent.trim().replace('× 10^', 'e')));
            values2.push(parseFloat(cells[1].textContent.trim().replace('× 10^', 'e')));
        }
    });

    return {
        labels,
        values1,
        values2
    };
}

// Функция для построения графика
function drawChart() {
    const data = parseData(); // Получаем данные из HTML

    const ctx = document.getElementById('myChart').getContext('2d');

    const chart = new Chart(ctx, {
        type: 'line',
        data: {

            labels: data.labels,
            datasets: [
                {
                    label: 'Значения 1',
                    data: data.values1,
                    fill: false,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 2
                },
                {
                    label: 'Значения 2',
                    data: data.values2,
                    fill: false,
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 2
                }
            ]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

