



function SendPostData(){
        console.log("функция работает ура");
        $.ajax({
            url: '/',
            dataType: 'text',
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            type: 'post',
            data: {"TitiChat":"1"},
            success: () =>{
            console.log("Завершение");
        },

    })
}



function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}