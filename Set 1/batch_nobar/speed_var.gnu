set term pngcairo

set output "speed_var.png"

set title "Pattern speed variation with time (snapshot)"
set yrange [2:-8]
set xlabel "Snapshot number"
set ylabel "Pattern speed ((km/s)/px)"

f1(x) = m1*x + c1
fit f1(x) "speed_var.dat" u 1:($3<=0.5 ? $2 : 1/0):3 yerrors via m1,c1
f2(x) = m2*x + c2
fit f2(x) "speed_var.dat" u 1:($5<=0.5 ? $4 : 1/0):5 yerrors via m2,c2
f3(x) = m3*x + c3
fit f3(x) "speed_var.dat" u 1:($7<=0.5 ? $6 : 1/0):7 yerrors via m3,c3

plot "speed_var.dat" u 1:($3<=0.5 ? $2 : 1/0):3 w yerrorbars pt 7 ps 1 lc "#ff0000" title "Slits 16 to 30",f1(x) lw 2 lc "#ff0000" title "", "speed_var.dat" u 1:($5<=0.5 ? $4 : 1/0):5 w yerrorbars pt 7 ps 1 lc "#00ff00" title "Slits 15 to -15",f2(x) lw 2 lc "#00ff00" title "", "speed_var.dat" u 1:($7<=0.5 ? $6 : 1/0):7 w yerrorbars pt 7 ps 1 lc "#0000ff" title "Slits -16 to -30",f3(x) lw 2 lc "#0000ff" title ""

set term wxt
