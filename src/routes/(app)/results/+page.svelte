<script>
	// @ts-nocheck
	import ResultsTable from './ResultsTable.svelte';

	import Hero from '$lib/components/page/Hero.svelte';
	import Content from '$lib/components/page/Content.svelte';

	import ResultCard from './ResultCard.svelte';

	export let data;

	import { base } from '$app/paths';
</script>

<svelte:head>
	<title>Results</title>
</svelte:head>

<Hero>IIOT 2025 Final Results</Hero>

<div class="w-full grow max-w-7xl px-4 gap-8 py-8 flex flex-col">
	<div class="gap-6 w-full flex-col flex md:hidden">
		{#each data.main_rows as row, i}
			<ResultCard
				hasTasks={data.hasTasks}
				year={data.year}
				{row}
				headers={data.headers}
				rank={i + 1}
			/>
		{/each}

		{#if data.guest_rows}
			<h2 class="text-3xl font-bold mt-4 text-center w-full">Guest Teams</h2>
			{#each data.guest_rows as row, i}
				<ResultCard
					hasTasks={data.hasTasks}
					year={data.year}
					{row}
					headers={data.headers}
					rank={i + 1}
				/>
			{/each}
		{/if}
	</div>

	<ResultsTable
		rows={data.main_rows}
		hasTasks={data.hasTasks}
		year={data.year}
		headers={data.headers}
	/>

	{#if data.guest_rows}
		<h2 class="hidden md:block text-3xl text-center font-bold mt-4">Guest Teams</h2>
		<ResultsTable
			rows={data.guest_rows}
			hasTasks={data.hasTasks}
			year={data.year}
			headers={data.headers}
		/>
	{/if}

	<div>
		<h2 class="text-3xl font-bold my-4 text-center">Complete Scoreboard</h2>
		<p class="text-lg text-center">
			For more detailed results data, you can see the CMS ranking <a
				href="{base}/ranking/"
				class="btn-link link-secondary">here</a
			>.
		</p>
	</div>
</div>
