const send_ga = () => {
//-- Universal analytics UA
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
   (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
   m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
   })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-124167090-6', 'auto');
  ga('send', 'pageview');

//-- GA4 with GTM
  (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
  new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayerGTM','GTM-TG454ZB');
}

let cookieAccepted = localStorage.cookieAccepted;
if (cookieAccepted == undefined) {
  $(document).ready(function () {
    var cookieDiv = document.createElement('div')
    cookieDiv.id = 'cookie-notice'
    cookieDiv.innerHTML = "<p style='margin: 1em'>Privacy and Cookies: This site uses cookies. By continuing to use this website, you agree to their use. To find out more, see our <a style='color:#4c71c6; text-decoration: underline;' href='https://cloud.dwavesys.com/leap/legal/privacy_policy/' target='_blank'>Privacy Policy</a>.<button id='cookie-accept' class='cookie-button'>Close and Accept</button></p>"

    $('body').append(cookieDiv).ready(() => {
      $('#cookie-notice').fadeIn('slow');
      $("#cookie-accept").click(function () {
        localStorage.setItem("cookieAccepted", true)
        $('#cookie-notice').fadeOut('slow');
        send_ga()
      });
    })
  })
} else if (cookieAccepted == "true") {
  send_ga()
}
