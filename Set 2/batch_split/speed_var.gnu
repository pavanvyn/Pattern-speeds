set term pngcairo

set output "speed_var.png"

dt = 0.06
omg_fac = -64/15
i = pi/6

set title "Pattern speed variation with time (snapshot)"
set yrange [0:40]
set xrange [0:14]
set xlabel "Evolution time (Gyr)"
set ylabel "Pattern speed ((km/s)/kpc)"

f1(x) = m1*x + c1
fit f1(x) "speed_var.dat" u ($1*dt):($3<=0.2 ? $2*omg_fac/sin(i) : 1/0):(-$3*omg_fac/sin(i)) yerrors via m1,c1
f2(x) = a2*exp(-b2*x)+c2
fit log(f2(x)) "speed_var.dat" u ($1*dt):($5<=0.2 ? log($4*omg_fac/sin(i)) : 1/0) via a2,b2,c2
b3 = 0.01
f3(x) = a3*exp(-b3*x)+c3
fit log(f3(x)) "speed_var.dat" u ($1*dt):($7<=0.2 ? log($6*omg_fac/sin(i)) : 1/0) via a3,b3,c3

plot f1(x) lw 2 lc "light-red" title "Slits 31 to 50 and -31 to -50",f2(x) lw 2 lc "medium-blue" title "Slits 11 to 30 and -11 to -30",f3(x) lw 2 lc "forest-green" title "Slits -10 to 10"

set output "speed_var_outer.png"
plot "speed_var.dat" u ($1*dt):($3<=0.2 ? $2*omg_fac/sin(i) : 1/0):(-$3*omg_fac/sin(i)) w yerrorbars pt 7 ps 1 lc "light-red" title "Slits 31 to 50 and -31 to -50",f1(x) lw 2 lc "light-red" title ""

set output "speed_var_intermed.png"
plot "speed_var.dat" u ($1*dt):($5<=0.2 ? $4*omg_fac/sin(i) : 1/0):(-$5*omg_fac/sin(i)) w yerrorbars pt 7 ps 1 lc "medium-blue" title "Slits 11 to 30 and -11 to -30",f2(x) lw 2 lc "medium-blue" title ""

set output "speed_var_inner.png"
plot "speed_var.dat" u ($1*dt):($7<=0.2 ? $6*omg_fac/sin(i) : 1/0):(-$7*omg_fac/sin(i)) w yerrorbars pt 7 ps 1 lc "forest-green" title "Slits -10 to -10",f3(x) lw 2 lc "forest-green" title ""



set ylabel "Log pattern speed ((km/s)/kpc)"
set yrange [0:5]

set output "speed_var_outer_log.png"
plot "speed_var.dat" u ($1*dt):($3<=0.2 ? log($2*omg_fac/sin(i)) : 1/0) pt 7 ps 1 lc "light-red" title "Slits 31 to 50 and -31 to -50",log(f1(x)) lw 2 lc "light-red" title ""

set output "speed_var_intermed_log.png"
plot "speed_var.dat" u ($1*dt):($5<=0.2 ? log($4*omg_fac/sin(i)) : 1/0) pt 7 ps 1 lc "medium-blue" title "Slits 11 to 30 and -11 to -30",log(f2(x)) lw 2 lc "medium-blue" title "

set output "speed_var_inner_log.png"
plot "speed_var.dat" u ($1*dt):($7<=0.2 ? log($6*omg_fac/sin(i)) : 1/0) pt 7 ps 1 lc "forest-green" title "Slits -10 to -10",log(f3(x)) lw 2 lc "forest-green" title ""

set term wxt
