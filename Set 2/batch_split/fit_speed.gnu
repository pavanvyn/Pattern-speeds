set term pngcairo

num_images = 221

set print "speed_var.dat"

do for [ind=0:num_images-1]{
	set title sprintf("Pattern speed %03d", ind)
	set xlabel "<x> (px)"
	set ylabel "<v_{los}> (km/s)"
	set output sprintf("speed_img/pattern_speed_%03d.png", ind)

	f1(x) = m1*x + c1
	fit f1(x) sprintf("speed_dat/pattern_speed_%03d.dat", ind) every ::1::20 u 1:2 via m1,c1
	f2(x) = m2*x + c2
	fit f2(x) sprintf("speed_dat/pattern_speed_%03d.dat", ind) every ::21::40 u 1:2 via m2,c2
	f3(x) = m3*x + c3
	fit f3(x) sprintf("speed_dat/pattern_speed_%03d.dat", ind) every ::41::61 u 1:2 via m3,c3
	f4(x) = m4*x + c4
	fit f4(x) sprintf("speed_dat/pattern_speed_%03d.dat", ind) every ::62::81 u 1:2 via m4,c4
	f5(x) = m5*x + c5
	fit f5(x) sprintf("speed_dat/pattern_speed_%03d.dat", ind) every ::82::101 u 1:2 via m5,c5

	plot sprintf("speed_dat/pattern_speed_%03d.dat", ind) every ::1::20 u 1:2 pt 7 ps 1.5 lc "light-red" title "Slits 31 to 50",f1(x) lw 2 lc "light-red" title "", sprintf("speed_dat/pattern_speed_%03d.dat", ind) every ::21::40 u 1:2 pt 7 ps 1.5 lc "dark-plum" title "Slits 11 to 30",f2(x) lw 2 lc "dark-plum" title "", sprintf("speed_dat/pattern_speed_%03d.dat", ind) every ::41::61 u 1:2 pt 7 ps 1.5 lc "forest-green" title "Slits -10 to -10",f3(x) lw 2 lc "forest-green" title "", sprintf("speed_dat/pattern_speed_%03d.dat", ind) every ::62::81 u 1:2 pt 7 ps 1.5 lc "dark-violet" title "Slits -11 to -30",f4(x) lw 2 lc "dark-violet" title "", sprintf("speed_dat/pattern_speed_%03d.dat", ind) every ::82::101 u 1:2 pt 7 ps 1.5 lc "medium-blue" title "Slits -31 to -50",f5(x) lw 2 lc "medium-blue" title ""

	print ind,"\t",m1,"\t",m1_err,"\t",m2,"\t",m2_err,"\t",m3,"\t",m3_err
	print ind,"\t",m5,"\t",m5_err,"\t",m4,"\t",m4_err,"\t",m3,"\t",m3_err
}

set print
set term wxt
