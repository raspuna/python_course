var weatherTable = {
    'Burbank' : [['cloudy', 21, 11], ['sunny', 25, 14], ['sunny', 31, 16], ['sunny', 32, 16]],
    'Chicago' : [['cloudy', 14, 8], ['cloudy', 14, 12], ['rainy', 13, 4], ['rainy', 6, 1]],
    'Dallas' : [['cloudy', 25, 16], ['rainy', 23, 11], ['sunny', 21, 7], ['sunny', 19, 3]]
}
var weatherImgs = {
    'Clouds' : './assets/some_clouds.png',
    'Rain' : './assets/some_rain.png',
    'Clear' : './assets/some_sun.png',
    'Snow' : './assets/some_clouds.png'
}
var weatherText = {
    'cloudy' : 'some clouds',
    'rainy' : 'some rain',
    'sunny' :  'some sun',
    'Clouds' : 'some clouds',
    'Clear' : 'some sun',
    'Rain' : 'some rain',
    'Snow' : 'some snow'
}
var coordinate = {
    'Los Angeles':'lat=34.024051&lon=-118.442617',
    'Chicago':'lat=41.881832&lon=-87.623177',
    'Burbank':'lat=34.180840&lon=-118.308968',
    'Dallas': 'lat=32.776665&lon=-96.796989'
}
var weatherIdx = ['today', 'tomorrow', 'Fri', 'Sat'];
var currentUnit = 'C';

function acceptCookie(element) {
    console.log(element.parentElement.parentElement);
    element.parentElement.parentElement.remove(); 
    return 0;
}

async function getWeatherAPI(cityName, currentUnit){
    var units =""
    if (currentUnit == 'F'){
        units = 'imperial'
    } else {
        units = 'metric'
    }

    var Response = await fetch("https://api.openweathermap.org/data/2.5/onecall?"+coordinate[cityName]+"&exclude=minutely,current,hourly&units="+ units + "&appid={API KEY}")
    var weatherData = await Response.json();
    console.log(weatherData)
    for (var i = 0; i < weatherIdx.length; i++){
        var tempData =[]
        tempData[0] = weatherData.daily[i].weather[0].main  /*weather text*/
        tempData[1] = weatherData.daily[i].temp.max
        tempData[2] = weatherData.daily[i].temp.min
        weatherTable[cityName][i] = tempData
    }
    return weatherData
}
async function drawWeather(cityName) {
    var weatherBox;
    console.log(currentUnit);
    var weatherData = await getWeatherAPI(cityName)
    for (var i = 0; i < weatherIdx.length; i++) {
        weatherBox = document.getElementById(weatherIdx[i]);
        weatherArr = weatherTable[cityName][i];
        console.log(weatherArr);
        /* change img src */
        weatherBox.childNodes[7].src = weatherImgs[weatherArr[0]];
        /* change weather explain text */
        weatherBox.childNodes[11].innerText = weatherText[weatherArr[0]];
        /* change temperature highest and lowest 
        highest - node[3]
        lowest - node[7]
        */
        temperature = weatherBox.childNodes[15];
        temperature.childNodes[3].innerText = transformToF(weatherArr[1], currentUnit) + "°";
        temperature.childNodes[7].innerText = transformToF(weatherArr[2], currentUnit) + "°";
    }
    return 0;
}
async function changeCity(cityName) {
    alert("Loading weather report..." + cityName);
    chosenCity = document.getElementById("chosen-city");
    chosenCity.innerText = cityName;
    await drawWeather(cityName);
    return 0;
}
function transformToF(num, indicator){
    if (indicator == 'F') {
        res = num * 1.8 + 32;
    } else {
        res = num;
    }
    return res.toFixed(0);
}
function transformBoth(num, indicator) {
    console.log(num);
    if (indicator == 'F') {
        res = num * 1.8 + 32;
    } else {
        res = (num - 32) / 1.8;
    }
    return res.toFixed(0);
}

function transform(element) {
    console.log(element.value);
    unitName = element.value;
    if (currentUnit != unitName) {
        currentUnit = unitName;
        for (var i = 0; i < weatherIdx.length; i++) {
            weatherBox = document.getElementById(weatherIdx[i]);
            temperature = weatherBox.childNodes[15];
            console.log(temperature.childNodes);
            /* trim ° */
            highest = temperature.childNodes[3].innerText.slice(0, -1); 
            lowest = temperature.childNodes[7].innerText.slice(0, -1);
            /* transform temperature by selector */
            temperature.childNodes[3].innerText = transformBoth(highest, unitName) + "°";
            temperature.childNodes[7].innerText = transformBoth(lowest, unitName) + "°";
        }
    }
    return 0;
}
