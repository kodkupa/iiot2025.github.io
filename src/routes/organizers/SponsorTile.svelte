<script lang="ts">
	import { base } from '$app/paths';
	import { onMount } from 'svelte';

	export let href: string;
	export let logo: string;
	export let alt: string;
	export let height: number;

	let img: HTMLImageElement;
	onMount(() => {
		img.style.height = `${height}rem`;
	});
</script>

<figure
	class="p-4 rounded-box hover:bg-base-300 hover:scale-[1.025] transition bg-opacity-75"
	data-theme="light"
>
	<a {href}>
		<img
			class="h-24 max-w-full object-contain"
			bind:this={img}
			src="{base}/images/logo/{logo}"
			{alt}
		/>
	</a>
</figure>
