<script>
	import Hero from '$lib/components/page/Hero.svelte';

	import htmlProgram from '$lib/Program.html?raw';
</script>

<svelte:head>
	<title>Schedule</title>
</svelte:head>

<Hero>Schedule</Hero>

<div class="px-4 py-8">
	{@html htmlProgram}
</div>

<style>
	:global(table thead) {
		display: none;
	}

	:global(table tbody tr th) {
		display: none;
	}
</style>
