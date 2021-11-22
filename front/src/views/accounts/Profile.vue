<template>
	<div id="profile_main">		
		<!-- 프로필 유저 이름, 닉네임, 랭크, 프로필 사진 등 -->
		<ProfileInfo
		class="d-block"
		/>
	</div>
</template>

<script>
// import axios from 'axios'
import ProfileInfo from '@/components/Profile/ProfileInfo'
export default {
	name: 'Profile',
	components: {
		ProfileInfo,
	},
}
</script>


<style>
h2 {
  color: black;
  font-weight: 200;
}
.navbar {
	border-radius: 0px;
	margin-bottom: 0px;
}


</style>