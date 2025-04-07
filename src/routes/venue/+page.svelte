<script>
	import { base } from '$app/paths';
	import Content from '$lib/components/page/Content.svelte';
	import Hero from '$lib/components/page/Hero.svelte';
</script>

<svelte:head>
	<title>Venue</title>
</svelte:head>

<Hero>Venue</Hero>
<Content>
	<h2 class="text-2xl sm:divider">Fazekas (contest venue)</h2>
	<p>
		The high school, which is the hungarian leader school of IIOT, is a more than 100-year-old
		inner-city school. Dozens of international science olympiads and other competitors have
		graduated from this school over the years. Its mathematics department is world-renowned. The
		opening and closing ceremonies will be held in the Great Hall (Nagyterem). The IIOT finals will
		be held in its computer labs.
		<br />
		<a href="https://fazekas.hu/" class="btn-link link-secondary">https://fazekas.hu/</a>
	</p>
	<h2 class="text-2xl sm:divider">Hotel</h2>
	<p>
		Accommodation will be in the <a
			href="https://all.accor.com/hotel/2025/index.en.shtml"
			class="btn-link link-secondary">Ibis Styles Budapest City</a
		>
		hotel on the banks of the Danube, near the Grand Boulevard (<a
			href="https://maps.app.goo.gl/iVVaWYMskifWAHBL6"
			class="btn-link link-secondary">Google Maps</a
		>). Double rooms will be available with wifi access.
	</p>
	<p>
		You can start your day with a standard buffet breakfast including Hungarian specialties (06:00 -
		10:00).
	</p>
	<p>Small shops and a variety of restaurants are located near the hotel.</p>
	<p>
		The accommodation is within walking distance of the contest venue, but also accessible by public
		transport (3+1 stops).
	</p>
	<h2 class="text-2xl sm:divider">Hungary information</h2>
	<p><b>Currency: </b>Hungarian Forint (HUF)</p>
	<p>
		The majority of shops and restaurants accept credit cards. <a
			href="https://www.triptobudapest.hu/hungarian-money-guide-how-to-pay-in-budapest/"
			class="btn-link link-secondary">More information.</a
		>
	</p>
	<p>
		<b>Power plugs: </b>220V, Type F (Schuko) or Type C (same as most of Europe).
		<a href="https://www.power-plugs-sockets.com/hungary/" class="btn-link link-secondary"
			>More information.</a
		>
	</p>
	<p>
		<b>Weather: </b>
		At the end of May and beginning of June, Hungary typically enjoys warm late spring weather, gradually
		transitioning into summer. Daytime highs: 23–30°C, Nighttime lows: 10–15°C. Often sunny or partly
		cloudy, but occasional showers or thunderstorms are common.
	</p>
	<p>
		See <a
			href="https://www.accuweather.com/en/hu/budapest/187423/daily-weather-forecast/187423"
			class="btn-link link-secondary">weather forecast</a
		>
		before traveling.
		<br />
		Local weather forecast with more details:
		<a href="https://www.idokep.hu/idojaras/Budapest" class="btn-link link-secondary">idokep.hu</a>
	</p>
	<p>
		<b> Transportation: </b>
		The public transportations system is good in Budapest. Route planning is available in Google Maps.
		Travel passes will be provided by the organizers to everyone. 
	</p>
	<p>
		<b> General information about Budapest: </b>
		<a href="https://en.wikipedia.org/wiki/Budapest" class="btn-link link-secondary"
			>Budapest Wikipedia</a
		>
		</p>
</Content>
