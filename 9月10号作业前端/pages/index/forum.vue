<template>
	<view class="content flex-column align-center" >
		<view class="into-item flex-row justify-around align-center" v-for="(item,index) in data":key="index">
			<view class="avatar-box align-center justify-center flex-row">
				<image class="avatar-image" :src="item.avatarUrl" mode="aspectFill"></image>
			</view>
			<view class="name-box flex-row justify-center">{{item.name}}</view>
			<view class="text-box flex-row align-center justify-between">
				{{item.text}}
			</view>
		</view>
		<view class="button-box">
			<button @click="post()">发帖</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				 title:'hello',
				 data:[
					 {
						 avatarUrl:'../../static/logo.png',
						 name:'sss',
						 text:'今天是九月十三号看合法后方哈加烽火流金佛哈弗我徽王府我和阿句法哈佛看被罚款',
					 },
					 {
						 avatarUrl:'../../static/logo.png',
						 name:'王凯韬',
						 text:'今天是九月十看被罚款',
					 }
				 ],
				 datalist:[]
			}
		},
		onShow(){
			this.getData()
		},
		methods: {
			post(){
				console.log('1');
				uni.navigateTo({
					url:"forumwrite"
				})
			},
			getData(){
				let that = this
				uni.request({
					url:'',
					method:'GET',
					header:{
						'Content-Type':''
					},
					data:{
						text:''
					},
					succes:(res) => {
						console.log(res.data)
						that.dataList = res.data.data.text
					}
				})
			}
		}
	}
	
</script>

<style>
	.content{
		min-height: 100vh;
		width: 100vw;
		background-color: antiquewhite;
	}
	.into-item{
		margin: 30rpx 0;
		height:200rpx;
		width: 675rpx;
		background-color: #fff;
		border-radius: 20px;
		box-shadow: 1px 2px 9px 0px #d2d1d1;
	}
	.avatar-box{
		margin-left: 20rpx;
		height: 100rpx;
		width: 100rpx;
	}
	.avatar-image{
		height:100rpx;
		width: 100rpx;
		border-radius: 50%;
	}
	.name-box{
		height: 100%;
		width: 40%;
		font-size :32rpx;
		margin-top: 65rpx;
	}
	.text-box{
		height: 80%;
		width: 100%;
	}
</style>
