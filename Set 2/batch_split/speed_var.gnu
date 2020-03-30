set term pngcairo

set output "speed_var.png"

set title "Pattern speed variation with time (snapshot)"
set xrange [0:225]
set yrange [0:3.5]
set xlabel "Snapshot number"
set ylabel "Pattern speed ((km/s)/px)"

f1(x) = m1*x + c1
fit f1(x) "speed_var.dat" u 1:($3<=0.2 ? $2 : 1/0):3 yerrors via m1,c1
f2(x) = -(a2*exp(-b2*x)+c2)
fit log(-f2(x)) "speed_var.dat" u 1:($5<=0.2 ? log(-$4) : 1/0) via a2,b2,c2
b3 = 0.01
f3(x) = -(a3*exp(-b3*x)+c3)
fit log(-f3(x)) "speed_var.dat" u 1:($7<=0.2 ? log(-$6) : 1/0) via a3,b3,c3

plot "speed_var.dat" u 1:($3<=0.2 ? -$2 : 1/0):3 w yerrorbars pt 7 ps 1 lc "light-red" title "Slits 31 to 50 and -31 to -50",-f1(x) lw 2 lc "light-red" title "", "speed_var.dat" u 1:($5<=0.2 ? -$4 : 1/0):3 w yerrorbars pt 7 ps 1 lc "medium-blue" title "Slits 11 to 30 and -11 to -30",-f2(x) lw 2 lc "medium-blue" title "", "speed_var.dat" u 1:($7<=0.2 ? -$6 : 1/0):7 w yerrorbars pt 7 ps 1 lc "forest-green" title "Slits -10 to 10",-f3(x) lw 2 lc "forest-green" title ""

set output "speed_var_outer.png"
plot "speed_var.dat" u 1:($3<=0.2 ? -$2 : 1/0):3 w yerrorbars pt 7 ps 1 lc "light-red" title "Slits 31 to 50 and -31 to -50",-f1(x) lw 2 lc "light-red" title ""

set output "speed_var_intermed.png"
plot "speed_var.dat" u 1:($5<=0.2 ? -$4 : 1/0):5 w yerrorbars pt 7 ps 1 lc "medium-blue" title "Slits 11 to 30 and -11 to -30",-f2(x) lw 2 lc "medium-blue" title ""

set output "speed_var_inner.png"
plot "speed_var.dat" u 1:($7<=0.2 ? -$6 : 1/0):7 w yerrorbars pt 7 ps 1 lc "forest-green" title "Slits -10 to -10",-f3(x) lw 2 lc "forest-green" title ""



set ylabel "Log pattern speed ((km/s)/px)"
set yrange [-3:3]

set output "speed_var_outer_log.png"
plot "speed_var.dat" u 1:($3<=0.2 ? log(-$2) : 1/0):3 w yerrorbars pt 7 ps 1 lc "light-red" title "Slits 31 to 50 and -31 to -50",log(-f1(x)) lw 2 lc "light-red" title ""

set output "speed_var_intermed_log.png"
plot "speed_var.dat" u 1:($5<=0.2 ? log(-$4) : 1/0):5 w yerrorbars pt 7 ps 1 lc "medium-blue" title "Slits 11 to 30 and -11 to -30",log(-f2(x)) lw 2 lc "medium-blue" title "

set output "speed_var_inner_log.png"
plot "speed_var.dat" u 1:($7<=0.2 ? log(-$6) : 1/0):7 w yerrorbars pt 7 ps 1 lc "forest-green" title "Slits -10 to -10",log(-f3(x)) lw 2 lc "forest-green" title ""

set term wxt
