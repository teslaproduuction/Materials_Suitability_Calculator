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
var data = [];

// База чтобы submit не руинил страницу
document.getElementById('myForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevents the default form submission
    calculate();
});

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
    try {
        flag = get_result[3];
        console.log("flag:", flag);
        if (flag === true) {
            console.log("Предупреждение:", flag);
            alert("Произошла ошибка. Проверьте введенные данные.");
            return;
        }

        data = get_result[2];

        var table = "<table class='table'>";
        table += "<thead><tr><th scope='col'>Номер критерия</th>";
        for (let i = 0; i < (get_result[0][0].length / 2); i++) {
            table += "<th scope='col'>Значение</th>";
        }
        table += "</tr></thead>";
        table += "<tbody>";

        for (i = 0; i < get_result[0].length; i++) {
            table += "<tr>";
            table += "<th scope='row' rowspan='2'>K" + (i + 1) + "</th>";

            if (get_result[0][0].length > 2) {
                for (var k = 0; k < get_result[0][i].length; k = k + 2) {
                    table += "<td>" + get_result[0][i][k] + "</td>";
                }
                table += "<td>" + get_result[1][i][1] + "</td>";
                table += "</tr><tr>";

                for (var k = 1; k < get_result[0][i].length; k = k + 2) {
                    table += "<td>" + get_result[0][i][k] + "</td>";
                }
                table += "<td>" + get_result[1][i][2] + "</td></tr>";
            }
        }
        table += "</tbody></table>";
        document.getElementById("result").innerHTML = table;
        console.log("Data1:", data);
        eel.clear()();
    } catch (error) {
        console.error("An error occurred:", error);
        alert("Произошла ошибка. Проверьте введенные данные.");
    }
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
            if (i + 1 === 10 || i + 1 === 11 || i + 1 === 12 || i + 1 === 13) {
                input.min = "0.0001";
                input.max = "1";
                input.step = "0.0001";
            } else {
                input.min = "0.0001";
                input.max = "10000";
                input.step = "0.0001";
            }
            input.className = "form-control text-right";
            input.id = "row" + (i + 1) + "col" + (columnIndex - 2 + j);
            input.required = " ";
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


// Функция для построения графика
var myChart; // Объявляем переменную myChart глобально, чтобы иметь доступ из функции drawChart

function drawChart() {
    try {
        const dataObject = JSON.parse(data);
        console.log('Данные:', dataObject);

        // Проверяем, существует ли график и является ли экземпляром Chart
        if (myChart instanceof Chart) {
            myChart.destroy();
        }

        // Показываем область графика
        document.getElementById('myChart').style.display = 'block';

        // Вызываем функцию createChart только после успешного получения данных
        createChart(dataObject);
    } catch (error) {
        console.error('Ошибка при разборе JSON:', error);
    }
}

function createChart(data) {
    var ctx = document.getElementById('myChart').getContext('2d');
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);

    var initialData = {
        labels: Object.keys(data),
        datasets: Object.keys(data[Object.keys(data)[0]]).map(function (key, index) {
            return {
                label: 'Сплав ' + (index + 1),
                data: Object.keys(data).map(function (criterion) {
                    return data[criterion][index];
                }),
                borderColor: '#' + Math.floor(Math.random() * 16777215).toString(16),
                borderWidth: 2,
                fill: false,
                pointStyle: 'circle',
                pointRadius: 3
            };
        })
    };

    myChart = new Chart(ctx, {
        type: 'line',
        data: initialData,
        options: {
            scales: {
                x: {
                    type: 'category',
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1
                    }
                },
                y: {
                    beginAtZero: true,
                    max: 10
                }
            },
            elements: {
                line: {
                    tension: 0
                }
            },
            plugins: {
                zoom: {
                    zoom: {
                        wheel: {
                            enabled: true
                        },
                        pinch: {
                            enabled: true
                        },
                        mode: 'xy'
                    }
                }
            },
        }
    });
}

// Не инициализируем график при загрузке страницы
// drawChart();
