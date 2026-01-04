Title: Maps
Slug: maps

It's weird how I ended up in synthetic aperture radar and scientific programming all because I took an "Introduction to GIS" course in undergrad. I just liked maps.

Most of my mapmaking lately involves products from high-resolution DEMs (a lot of my inspiration comes from the [WA DNR "Bare Earth" hillshades](https://wadnr.maps.arcgis.com/apps/Cascade/index.html?appid=36b4887370d141fcbb35392f996c82d9)) trying to capture the topography of different features on Earth. Mostly volcanoes, if I'm being honest. I grew up on ArcPro some years ago, but I've started to realize I can pull off the same things with QGIS and free image editing software. If Gerardus Mercator managed with ink and paper, I figure I can handle it without a bajillion-dollar license.

I wish I had more to share here from my efforts in [conservation planning](https://www.wm.edu/offices/iic/news/iic-conservation-gis-lab-contributes-to-key-biodiversity-area-planning-knowledge.php) and [mapping racial gerrymandering](https://news.wm.edu/2022/10/11/wm-professors-unveil-new-model-to-measure-segregation-in-voting-districts/), but this page is sparse for now.


## **Volcanoes**

### *Universidad de Colima, Colima Intercambio e Investigación en Vulcanología*

In loose collaboration with the Universidad de Colima's [University Center for Volcanological Studies](https://portal.ucol.mx/cueiv/), I develop hazard maps for the estimated effects of the 1913 VEI-4 Sub-Plinian Eruption of Volcán de Colima on modern day infrastructure and population.

<figure style="max-width:120ch; margin:0.8em auto; text-align:center; position:relative;">
  <div id="ciiv-carousel" style="position:relative; width:100%; overflow:hidden; border-radius:6px;">
    <button class="ciiv-fs-toggle" title="Toggle fullscreen" aria-label="Toggle fullscreen"
            style="position:absolute; right:8px; top:8px; z-index:10; background:rgba(255,255,255,0.85); border:0; padding:6px; border-radius:4px; cursor:pointer;">
      ⤢
    </button>

    <div class="ciiv-slides" style="display:flex; transition:transform 350ms ease; will-change:transform;">
      <img src="../images/ciiv_carousel/oblique_municipalities_no_vei4.png" alt="Oblique municipalities map" style="width:100%; flex-shrink:0; object-fit:cover;" />
      <img src="../images/ciiv_carousel/oblique_municipalities_vei4_hs.png" alt="Hillshade and VEI-4 map" style="width:100%; flex-shrink:0; object-fit:cover;" />
      <img src="../images/ciiv_carousel/opposite_oblique.png" alt="Opposite oblique view" style="width:100%; flex-shrink:0; object-fit:cover;" />
    </div>

    <button class="ciiv-prev" aria-label="Previous" style="position:absolute; left:6px; top:50%; transform:translateY(-50%); z-index:10; background:rgba(0,0,0,0.45); color:#fff; border:0; padding:6px 8px; border-radius:4px; cursor:pointer;">‹</button>
    <button class="ciiv-next" aria-label="Next" style="position:absolute; right:6px; top:50%; transform:translateY(-50%); z-index:10; background:rgba(0,0,0,0.45); color:#fff; border:0; padding:6px 8px; border-radius:4px; cursor:pointer;">›</button>

    <div class="ciiv-indicators" style="position:absolute; left:50%; transform:translateX(-50%); bottom:8px; z-index:10; display:flex; gap:6px;">
      <button data-index="0" aria-label="Slide 1" style="width:10px; height:10px; background:rgba(255,255,255,0.8); border-radius:50%; border:0; padding:0; cursor:pointer;"></button>
      <button data-index="1" aria-label="Slide 2" style="width:10px; height:10px; background:rgba(255,255,255,0.5); border-radius:50%; border:0; padding:0; cursor:pointer;"></button>
      <button data-index="2" aria-label="Slide 3" style="width:10px; height:10px; background:rgba(255,255,255,0.5); border-radius:50%; border:0; padding:0; cursor:pointer;"></button>
    </div>
  </div>

  <figcaption style="font-style:italic; font-size:0.82em; margin-top:0.25em; color:#555;">
    Map drafts from the CIIV collaboration
  </figcaption>
</figure>

<script>
(function() {
  const container = document.getElementById('ciiv-carousel');
  if (!container) return;

  const slides = container.querySelector('.ciiv-slides');
  const imgs = slides.querySelectorAll('img');
  const prev = container.querySelector('.ciiv-prev');
  const next = container.querySelector('.ciiv-next');
  const indicators = container.querySelectorAll('.ciiv-indicators button');
  const fsToggle = container.querySelector('.ciiv-fs-toggle');

  let idx = 0;
  const total = imgs.length;

  function update() {
    slides.style.transform = 'translateX(' + (-idx * 100) + '%)';
    indicators.forEach((b,i)=> b.style.background = i===idx ? 'rgba(255,255,255,0.95)' : 'rgba(255,255,255,0.5)');
  }

  prev.addEventListener('click', ()=> { idx = (idx - 1 + total) % total; update(); });
  next.addEventListener('click', ()=> { idx = (idx + 1) % total; update(); });
  indicators.forEach(b => b.addEventListener('click', e => { idx = Number(e.currentTarget.dataset.index); update(); }));

  // Keyboard left/right when focused
  container.tabIndex = 0;
  container.addEventListener('keydown', e => {
    if (e.key === 'ArrowLeft') prev.click();
    if (e.key === 'ArrowRight') next.click();
  });

  // Fullscreen toggle
  fsToggle.addEventListener('click', async () => {
    if (!document.fullscreenElement) {
      try { await container.requestFullscreen(); }
      catch (err) { console.warn('Fullscreen failed:', err); }
    } else {
      try { await document.exitFullscreen(); }
      catch (err) { console.warn('Exit fullscreen failed:', err); }
    }
  });

  // Resize images to match container aspect ratio on fullscreen
  function onFullChange() {
    if (document.fullscreenElement) {
      container.style.maxWidth = 'none';
      container.style.width = '100%';
    } else {
      container.style.maxWidth = '';
      container.style.width = '';
    }
  }
  document.addEventListener('fullscreenchange', onFullChange);

  // Initialize
  update();
})();
</script>
