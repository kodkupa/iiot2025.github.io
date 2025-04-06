<script>
	import Hero from '$lib/components/page/Hero.svelte';
	import Content from '$lib/components/page/Content.svelte';
	import Date from './Date.svelte';
	import { base } from '$app/paths';
</script>

<svelte:head>
	<title>Schedule</title>
</svelte:head>

<Hero>Schedule</Hero>

<Content>
	<p class="mx-auto">
		Deadline for <a href="{base}/registration" class="btn-link link-secondary">registration</a> of teams
		and delegation members is April 30.
	</p>
	<h2 class="text-2xl sm:divider">Schedule for contest days</h2>
	<p>A detailed schedule will be published at least two weeks before the contest.</p>
</Content>
<div class="max-w-xl w-full flex flex-col text-center gap-4">
	<Date>
		<h2 slot="title">May 30 (Friday)</h2>
		<p slot="date">Arrivals @Hotel (from 15:00). Dinner will be provided.</p>
	</Date>
	<Date>
		<h2 slot="title">May 31 (Saturday)</h2>
		<p slot="date">Opening Ceremony @Fazekas & Practice contest @Fazekas</p>
	</Date>
	<Date>
		<h2 slot="title">June 1 (Sunday)</h2>
		<p slot="date">Contest @Fazekas</p>
	</Date>
	<Date>
		<h2 slot="title">June 2 (Monday)</h2>
		<p slot="date">Sightseeing @Budapest & Closing Ceremony @Fazekas</p>
	</Date>
	<Date>
		<h2 slot="title">June 3 (Tuesday)</h2>
		<p slot="date">Departures @Hotel (until 12:00, breakfast will be provided)</p>
	</Date>
</div>
