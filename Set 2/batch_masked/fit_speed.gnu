set term pngcairo

num_images = 221

set print "speed_var.dat"

do for [ind=0:num_images-1]{
	set title sprintf("Pattern speed %03d", ind)
	set xlabel "<x> (px)"
	set ylabel "<v_{los}> (km/s)"
	set output sprintf("speed_img/pattern_speed_%03d.png", ind)

	f(x) = m*x + c
	fit f(x) sprintf("speed_dat/pattern_speed_%03d.dat", ind) u 1:2 via m,c
	plot sprintf("speed_dat/pattern_speed_%03d.dat", ind) u 1:2 pt 7 ps 1.5 lc "forest-green",f(x) lw 2 lc "forest-green"

	print ind,"\t",m,"\t",m_err
}

set print
set term wxt
