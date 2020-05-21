set term pngcairo

set output "actual_speed.png"

dt = 1.5*0.025
omg_fac = -3.2
i = pi/6

set title "Pattern speed variation with time (snapshot)"
set yrange [10:50]
set xlabel "Evolution time (Gyr)"
set ylabel "Pattern speed ((km/s)/kpc)"

f(x) = m*x + c
fit f(x) "speed_var.dat" u ($1*dt):($3<=0.5 ? $2*omg_fac/sin(i) : 1/0):(-$3*omg_fac/sin(i)) yerrors via m,c
g(x) = n*x + d
fit g(x) "iomegaB.dat" u 1:2 via n,d
plot "speed_var.dat" u ($1*dt):($3<=0.5 ? $2*omg_fac/sin(i) : 1/0):(-$3*omg_fac/sin(i)) w yerrorbars pt 7 ps 1 lc "forest-green" title "TW method", f(x) lw 2 lc "forest-green" title "", "iomegaB.dat" u 1:2 pt 7 ps 1 lc "black" title "Fourier method (from simulation)", g(x) lw 2 lc "black" title ""

set term wxt
