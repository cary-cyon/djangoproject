let audio = document.getElementById("audio");    // Берём элемент audio
let time = document.querySelector(".time");      // Берём аудио дорожку
let btnPlay = document.querySelector(".play");   // Берём кнопку проигрывания
let btnPause = document.querySelector(".pause"); // Берём кнопку паузы



let playlist = [
    'Violet_aud_bl7QfDF.mp3',
    'forestfloor_aud_hScxzPq.mp3'
];

let treck; // Переменная с индексом трека

// Событие перед загрузкой страницы
window.onload = function() {
    treck = 0; // Присваиваем переменной ноль
};
function switchTreck (numTreck) {
    // Меняем значение атрибута src
    audio.src = '/media/audios/' + playlist[numTreck];
    // Назначаем время песни ноль
    audio.currentTime = 0;
    // Включаем песню
    audio.play();
};
//для копки начать
btnPlay.addEventListener("click", function() {
    audio.play(); // Запуск песни
    // Запуск интервала
    audioPlay = setInterval(function() {
        // Получаем значение на какой секунде песня
        let audioTime = Math.round(audio.currentTime);
        // Получаем всё время песни
        let audioLength = Math.round(audio.duration)
        // Назначаем ширину элементу time
        time.style.width = (audioTime * 100) / audioLength + '%';
        // Сравниваем, на какой секунде сейчас трек и всего сколько времени длится
        // И проверяем что переменная treck меньше четырёх
        if (audioTime == audioLength && treck < playlist.length -1) {
            treck++; // То Увеличиваем переменную
            switchTreck(treck); // Меняем трек
        // Иначе проверяем тоже самое, но переменная treck больше или равна четырём
        } else if (audioTime == audioLength && treck >= playlist.length -1) {
            treck = 0; // То присваиваем treck ноль
            switchTreck(treck); // Меняем трек
        }
    }, 10)
});
//для кнопки паузы
btnPause.addEventListener("click", function() {
    audio.pause(); // Останавливает песню
    clearInterval(audioPlay) // Останавливает интервал
});
