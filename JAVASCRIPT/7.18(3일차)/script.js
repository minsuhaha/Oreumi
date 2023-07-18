// function loadMovieInfo(){
//     // 사용자가 검색을 한 영화 제목 가져오기
//     let movieTitle = document.querySelector('#movieTitle').value;
//     if (movieTitle === '') {
//         alert('영화 제목을 입력해주세요.');
//         return;
//     }

//      // 영화 데이터 가져오기
//      // XMLHttpRequest -> get/post 방식 요청을 보내는
//     let xhr = new XMLHttpRequest();
//     xhr.onreadystatechange = function(){
//         if (xhr.readyState === 'XMLHttpRequest.DONE'){
//             if (xhr.status === 200) {
//                 let data = Json.parse(xhr.responseText)
//                 if (data.Reponse === 'False') {
//                     alert('영화 정보를 가져오는데 실패했습니다.');
//                 } else {
//                     let movieInfo = '';
//                     movieInfo += '<h2>' + data.Title + '</h2>';
//                     movieInfo += '<p><strong>장르:</strong>' + data.Genre + '</p>';
//                     movieInfo += '<p><strong>감독:</strong>' + data.Director + '</p>';
//                     movieInfo += '<p><strong>배우:</strong>' + data.Actors + '</p>';
//                     document.getElementById('movieInfo').innerHTML = movieInfo;
//                 }

//             } else {
//                 alert('영화 정보를 가져오는데 실패했습니다!');
//             }
//         }
//     };

//    xhr.open('GET', 'https://www.omdbapi.com/?i=tt3896198&apikey=30f66621&t=' + 
//    encodeURIComponent(movieTitle), true);
//    xhr.send();
// }

function loadMovieInfo(){
    let movieTitle = document.getElementById("movieTitle").value; // 영화 제목 가져옴
    if (movieTitle === ''){
        alert('영화 제목을 입력해주세요.');
        return;
    }

    // 외부 통신 시 XMLHttpRequest를 사용
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function(){
        if (xhr.readyState === XMLHttpRequest.DONE){
            if (xhr.status === 200){
                let data = JSON.parse(xhr.responseText)
                // console.log(data)
                if (data.Response === 'False'){
                    alert('영화 정보를 가져오는데 실패했습니다.');
                } else{
                    let movieInfo = '';
                    movieInfo += '<h2>' + data.Title + '</h2>';
                    movieInfo += '<p><strong>장르:</strong>'+ data.Genre + '</p>';
                    movieInfo += '<p><strong>감독:</strong>'+ data.Director + '</p>';
                    movieInfo += '<p><strong>배우:</strong>'+ data.Actors + '</p>';
                    movieInfo += '<p><strong>포스터 : </strong>' + '<img src = ' + data.Poster + '></p>'; 
                    document.getElementById('movieInfo').innerHTML = movieInfo;
                }
            } else {
                alert('영화 정보를 가져오는데 실패했습니다.');
            }
        } 
    };
    xhr.open('GET', 'https://www.omdbapi.com/?i=tt3896198&apikey=30f66621&t=' + encodeURIComponent(movieTitle), true);
    xhr.send();
}

