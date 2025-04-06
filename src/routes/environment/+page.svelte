<script>
	import Hero from '$lib/components/page/Hero.svelte';
	import Content from '$lib/components/page/Content.svelte';
</script>

<svelte:head>
	<title>Environment</title>
</svelte:head>

<Hero>Contest Environment</Hero>

<Content>
	<h2 class="text-2xl sm:divider">Software</h2>
	<p>Contestants can expect the following software, with the minimum versions stated below.</p>
	<p>
		<b>Operating System: </b>
		Windows 10 (Windows_NT x64 10.0.19045)
	</p>
	<p>
		<b>Compiler: </b>
		Mingw-w64 GCC (xxx)
	</p>
	<div>
		<b>Text Editors and IDEs:</b>
		<ul class="list-disc ml-12">
			<li>CLion (xxx)</li>
			<li>Code::Blocks (20.03) *</li>
			<li>Visual Studio Code (1.58.2)</li>
		</ul>
	</div>
	<p>
		* Code::Blocks has known stability issues, so it is not recommended to use, and no extra time
		will be provided to teams who lose time because of Code::Blocks related problems.
	</p>
	<h2 class="text-2xl sm:divider">Grading System</h2>
	<p>
		Contest Management System (<a href="https://cms-dev.github.io/" class="btn-link link-secondary"
			>CMS</a
		>) will be used as the grading system.
	</p>
	<p>
		The exact commands used for compilation will be shown on the grading system. With the exception
		of certain task types, the compilation command will generally be of the following format:
	</p>
	<code>/usr/bin/g++ -DEVAL -std=c++20 -xc++ -O2 -pipe -static -s -o task task.cpp -lm </code>
	<p>
		The operating system of the grading machine is Ubuntu 24.04. The C++ compiler version is GCC
		13.3.0.
	</p>
</Content>
