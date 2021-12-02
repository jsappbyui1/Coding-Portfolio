if o_player.dead == true or o_player.state = "idle" {
	hspeed = 0
}else{hspeed = store_speed}


if x < 0 {
	image_alpha = .01
	x = 352
}
