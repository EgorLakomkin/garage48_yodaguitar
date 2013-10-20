/**
 * Created by anton on 20.10.13.
 */

app = {

    playerState : 0,
    startPlaying : function(){
        var src =  "/static/img/refresh.png"

            playSong();
            app.playerState = 1;
            var image=$("#play-btn");
            $("#play-btn").fadeOut('fast', function(){
                image.attr('src', src);
                image.fadeIn('fast');
            });
    //    alert(app.playerState+" start");
            //$(this).attr('src', src);
	startRecording();
    },
    stoppedPlaying : function(){//callback from canvas
        app.playerState = 0;
        var src = "/static/img/play.png";
        {

            var image=$("#play-btn");
            $("#play-btn").fadeOut('fast', function(){
                image.attr('src', src);
                image.fadeIn('fast');
            });
      //      alert(app.playerState+" stop");
	    stopRecording();
            //$(this).attr('src', src);
        }
    },
    onPlayBtnClick : function(){
//        if(app.playerState == 0){
//            app.startPlaying();
//        }
//        if(app.playerState == 1){
//            stopSong();
//        }
        switch (app.playerState){
            case 0 : app.startPlaying(); break;
            case 1 :  stopSong(); break;
        }
    },
    test:function(){
     alert("sdfsdf");
    }

}