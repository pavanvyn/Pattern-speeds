set term pngcairo

num_images = 57

set print "speed_var.dat"

do for [ind=0:num_images-1]{
	set title sprintf("Pattern speed %03d", ind)
	set xlabel "<x> (px)"
	set ylabel "<v_{los}> (km/s)"
	set output sprintf("speed_img/pattern_speed_%03d.png", ind)

	f1(x) = m1*x + c1
	fit f1(x) sprintf("speed_dat/pattern_speed_%03d.dat", ind) every ::1::15 u 1:2 via m1,c1
	f2(x) = m2*x + c2
	fit f2(x) sprintf("speed_dat/pattern_speed_%03d.dat", ind) every ::16::46 u 1:2 via m2,c2
	f3(x) = m3*x + c3
	fit f3(x) sprintf("speed_dat/pattern_speed_%03d.dat", ind) every ::47::61 u 1:2 via m3,c3

	plot sprintf("speed_dat/pattern_speed_%03d.dat", ind) every ::1::15 u 1:2 pt 7 ps 1.5 lc "light-red" title "Slits 16 to 30",f1(x) lw 2 lc "light-red" title "", sprintf("speed_dat/pattern_speed_%03d.dat", ind) every ::16::46 u 1:2 pt 7 ps 1.5 lc "forest-green" title "Slits 15 to -15",f2(x) lw 2 lc "forest-green" title "", sprintf("speed_dat/pattern_speed_%03d.dat", ind) every ::47::61 u 1:2 pt 7 ps 1.5 lc "medium-blue" title "Slits -16 to -30",f3(x) lw 2 lc "medium-blue" title ""

	print ind,"\t",m1,"\t",m1_err,"\t",m2,"\t",m2_err
	print ind,"\t",m3,"\t",m3_err,"\t",m2,"\t",m2_err
}

set print
set term wxt
