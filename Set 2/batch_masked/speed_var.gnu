set term pngcairo

set output "speed_var.png"

set title "Pattern speed variation with time (snapshot)"
unset key
set yrange [0:-3.5]
set xrange [0:225]
set xlabel "Snapshot number"
set ylabel "Pattern speed ((km/s)/px)"

f(x) = m*x + c
fit f(x) "speed_var.dat" u 1:($3<=0.2 ? $2 : 1/0):3 yerrors via m,c
plot "speed_var.dat" u 1:($3<=0.2 ? $2 : 1/0):3 w yerrorbars pt 7 ps 1 lc "forest-green",f(x) lw 2 lc "forest-green"

set term wxt
