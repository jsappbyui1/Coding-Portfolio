/// @description Insert description here
// You can write your code in this editor
if o_player.state = "active"{
	image_alpha = 1
}
image_index = round(score/place)
if 1 = score/(place*10){
	
	inst = instance_create_layer(x-5,y,"Instances",o_scoreboard)
	x += 5
	inst.place = place*10

	}
