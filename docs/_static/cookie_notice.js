const send_ga = () => {
//-- GA4 with GTM
(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayerGTM','GTM-TG454ZB');
}

let cookieAccepted = localStorage.getItem('cookieAccepted');

if (cookieAccepted === null) {
document.addEventListener('DOMContentLoaded', function () {
  var cookieDiv = document.createElement('div');
  cookieDiv.id = 'cookie-notice';
  cookieDiv.innerHTML = "<p style='margin: 1em'>Privacy and Cookies: This site uses cookies. By continuing to use this website, you agree to their use. To find out more, see our <a style='color:#4c71c6; text-decoration: underline;' href='https://cloud.dwavesys.com/leap/legal/privacy_policy/' target='_blank'>Privacy Policy</a>.<button id='cookie-accept' class='cookie-button'>Close and Accept</button></p>";

  document.body.appendChild(cookieDiv);
  
  document.getElementById('cookie-accept').addEventListener('click', function () {
	localStorage.setItem('cookieAccepted', 'true');
	document.getElementById('cookie-notice').style.display = 'none';
	send_ga();
  });
  
  document.getElementById('cookie-notice').style.display = 'block';
});
} else if (cookieAccepted === 'true') {
send_ga();
}
