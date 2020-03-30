set term pngcairo

set output "actual_speed.png"

dt = 1.5
t_fac = 0.02492
omg_fac = -3.2
i = pi/6

set title "Pattern speed variation with time (snapshot)"
set yrange [10:50]
set xlabel "Snapshot number"
set ylabel "Pattern speed ((km/s)/kpc)"

f(x) = m*x + c
fit f(x) "speed_var.dat" u 1:($3<=0.5 ? $2*omg_fac/sin(i) : 1/0):3 yerrors via m,c
g(x) = n*x + d
fit g(x) "iomegaB.dat" u ($1/(dt*t_fac)):2 via n,d
plot "speed_var.dat" u 1:($3<=0.5 ? $2*omg_fac/sin(i) : 1/0):3 w yerrorbars pt 7 ps 1 lc "#000000" title "TW method", f(x) lw 2 lc "#000000" title "", "iomegaB.dat" u ($1/(dt*t_fac)):2 pt 7 ps 1 lc "#00ff00" title "Fourier method (from simulation)", g(x) lw 2 lc "#00ff00" title ""

set term wxt
