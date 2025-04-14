<script>
	import { base } from '$app/paths';

	export let title;
	export let image;
</script>

<div
	class="card bg-base-200 w-full sm:max-w-sm shadow-sm border border-base-content border-opacity-10"
>
	<figure class="p-4">
		<img src="{base}/images/logo/{image}" alt="{title} logo" class="max-h-52" />
	</figure>
	<div class="card-body pt-0">
		<h2 class="card-title">{title}</h2>
		<p class="text-justify">
			<slot>Description</slot>
		</p>
	</div>
</div>
