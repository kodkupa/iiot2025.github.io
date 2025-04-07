<script>
	import { clickOutside } from '$lib/scripts/clickOutside';
	import { createEventDispatcher } from 'svelte';

	import { base } from '$app/paths';
	import { page } from '$app/stores';

	const dispatch = createEventDispatcher();

	let dropdownOpened = false;
	function closeDropdown() {
		dropdownOpened = false;
	}

	function closeDrawer() {
		dropdownOpened = false;
		dispatch('closeDrawer');
	}
</script>

<li>
	<a href="{base}/" class:font-bold={$page.route.id === `${base}/`} on:click={closeDrawer}>Home</a>
</li>
<li>
	<details bind:open={dropdownOpened} use:clickOutside on:outsideclick={closeDropdown}>
		<summary>Competition</summary>
		<ul class="p-2">
			<li>
				<a
					href="{base}/environment/"
					class:font-bold={$page.route.id === `${base}/environment/`}
					on:click={closeDrawer}>Environment</a
				>
			</li>
			<li>
				<a
					href="{base}/rules/"
					class:font-bold={$page.route.id === `${base}/rules/`}
					on:click={closeDrawer}
				>
					Rules
				</a>
			</li>
			<li />
			<li>
				<a
					href="{base}/participants/"
					class:font-bold={$page.route.id === `${base}/participants/`}
					on:click={closeDrawer}>Participants</a
				>
			</li>
			<li />
			<li>
				<a
					href="{base}/tasks/"
					class:font-bold={$page.route.id === `${base}/tasks/`}
					on:click={closeDrawer}>Tasks</a
				>
			</li>
			<li>
				<a
					href="{base}/results/"
					class:font-bold={$page.route.id === `${base}/results/`}
					on:click={closeDrawer}>Results</a
				>
			</li>
		</ul>
	</details>
</li>
<li>
	<a
		href="{base}/venue/"
		class:font-bold={$page.route.id === `${base}/venue/`}
		on:click={closeDrawer}>Venue</a
	>
</li>
<li>
	<a
		href="{base}/schedule/"
		class:font-bold={$page.route.id === `${base}/schedule/`}
		on:click={closeDrawer}>Schedule</a
	>
</li>
<li>
	<a
		href="{base}/organizers/"
		class:font-bold={$page.route.id === `${base}/organizers/`}
		on:click={closeDrawer}>Organizers</a
	>
</li>
<li>
	<a
		href="{base}/registration/"
		class:font-bold={$page.route.id === `${base}/registration/`}
		on:click={closeDrawer}>Registration</a
	>
</li>

<style>
	summary::after {
		color: hsl(var(--bc)) !important;
	}
</style>
