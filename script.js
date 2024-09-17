function toggleSeries(level) {
    const fundamentalSeries = document.getElementById('fundamental-series');
    const medioSeries = document.getElementById('medio-series');

    if (level === 'Ensino Fundamental') {
        fundamentalSeries.style.display = 'block';
        medioSeries.style.display = 'none';
    } else if (level === 'Ensino Médio') {
        fundamentalSeries.style.display = 'none';
        medioSeries.style.display = 'block';
    } else {
        fundamentalSeries.style.display = 'none';
        medioSeries.style.display = 'none';
    }
}
