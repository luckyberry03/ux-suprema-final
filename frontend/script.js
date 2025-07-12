fetch('https://ux-suprema-final-backend.onrender.com/api/halo')
  .then(res => res.json())
  .then(data => {
    document.getElementById("hasil").textContent = data.pesan;
  })
  .catch(() => {
    document.getElementById("hasil").textContent = "Gagal hubungi backend.";
  });
