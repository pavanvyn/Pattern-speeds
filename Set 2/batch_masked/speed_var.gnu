set term pngcairo

set output "speed_var.png"

dt = 0.06
omg_fac = -64/15
i = pi/6

set title "Pattern speed variation with time (snapshot)"
set yrange [0:25]
set xrange [0:14]
set xlabel "Evolution time (Gyr)"
set ylabel "Pattern speed ((km/s)/kpc)"

f(x) = m*x + c
fit f(x) "speed_var.dat" u ($1*dt):($3<=0.2 ? $2*omg_fac/sin(i) : 1/0):(-$3*omg_fac/sin(i)) yerrors via m,c
plot "speed_var.dat" u ($1*dt):($3<=0.2 ? $2*omg_fac/sin(i) : 1/0):(-$3*omg_fac/sin(i)) w yerrorbars pt 7 ps 1 lc "forest-green" title "Slits -25 to -25 masked",f(x) lw 2 lc "forest-green" title ""

set term wxt
