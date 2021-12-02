
function flap(){
	o_player.image_index = 0
	if (o_player.state != "idle"){
	audio_play_sound(wing,1,false); 
	}
	
	o_player.vspeed = -5;
	
}

function game_over(){
	if (o_player.dead = false){
		audio_play_sound(hit,1,false);
		o_player.dead = true
	}
	o_player.vspeed = 0
	o_player.y -= 1;

}
