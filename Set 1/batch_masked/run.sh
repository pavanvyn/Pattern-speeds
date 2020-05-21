mkdir speed_img

python imdisplay.py
echo "Image profiles display done"
python profile.py
echo "Lmask_ine profiles extraction done"
python interpolate.py
echo "Line profiles interpolation done"
python integrate.py
echo "Pattern speed integration done"

rm fit.log
gnuplot fit_speed.gnu

gnuplot speed_var.gnu

python histogram.py
python histogram_compare.py
