document.addEventListener('DOMContentLoaded', () => {
  // Probar formulario del gateway
  const form = document.getElementById('form-proxy');
  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const fd = new FormData(form);
      const method = fd.get('method') || 'GET';
      const path = fd.get('path') || '/health';
      let body = fd.get('body');
      let options = { method, headers: {} };
      if (body && body.trim().length > 0) {
        try {
          JSON.parse(body);
          options.headers['Content-Type'] = 'application/json';
          options.body = body;
        } catch {
          alert('El body debe ser JSON válido.');
          return;
        }
      }
      const respEl = document.getElementById('proxy-response');
      respEl.textContent = 'Cargando...';
      try {
        const res = await fetch(`${GATEWAY_URL}${path}`);
        const text = await res.text();
        respEl.textContent = text;
      } catch (err) {
        respEl.textContent = String(err);
      }
    });
  }
});