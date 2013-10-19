/**
 * Created by anton on 20.10.13.
 */

app = {

    playerState : 0,
    startPlaying : function(){
        var src =  "/static/img/refresh.png"

            playSong();
            app.playerState = 1;
            var image=$(this);
            $(this).fadeOut('fast', function(){
                image.attr('src', src);
                image.fadeIn('fast');
            })
            //$(this).attr('src', src);

    },
    stoppedPlaying : function(){//callback from canvas
        app.playerState = 0;
        var src = "/static/img/play.png";
        {

            var image=$(this);
            $(this).fadeOut('fast', function(){
                image.attr('src', src);
                image.fadeIn('fast');
            })
            //$(this).attr('src', src);
        }
    },
    onPlayBtnClick : function(){
        if(app.playerState == 0){
            app.startPlaying();
        }
        if(app.playerState == 1){
            stopSong();
        }
    }

}