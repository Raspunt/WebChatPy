


function SendPostData(){
        console.log("функция работает ура");
        $.ajax({
            url: '/',
            dataType: 'text',
            type: 'post',
            data: "createChat",
            success: () =>{
            console.log("Завершение");
        },

    })
}