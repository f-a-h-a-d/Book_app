<template>
    <body>
    <div class="main-container">
      <div class="row">
        <sideBar/>
        <main class="col-9">
          <div class="top">
            <span class="dropdown show"><img src="./images/Notification.png" alt="">
              <!-- <a>Mr. Mofiz <img src="./images/Ellipse 265.png" alt=""></a>
              <select name="" id="">
                <option value="1" data-image="./images/Ellipse 265.png">Mr. Mofiz</option>
            </select> -->
            <button class="dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Mr. Mofiz <img src="./images/Ellipse 265.png" alt="">

              <div class="user-dropdown">
                <h3>Welcome to Fiz</h3>
                <ul class="user-info-links">
                  <li>
                    <i class=""></i>
                    <a href="">Profile</a>
                  </li>
                  <li>
                    <i class=""></i>
                    <a href="">Message</a>
                  </li>
                  <li>
                    <i class=""></i>
                    <a href="">Notification</a>
                  </li>
                </ul>
                <ul class="settings-icon">
                  <li>
                    <i class=""></i>
                    <a href="">Settings</a>
                  </li>
                  <li>
                    <i class=""></i>
                    <a href="">Logout</a>
                  </li>
                </ul>
              </div>

            </button>
            
            </span>
          </div>
          
          <section class="right-side-content-area">
            <div class="table-top">
              <h3>Disputes</h3>
              <div>
                <input
                  type="text"
                  placeholder="&#xF002; Search here"
                />
                <button type="">+ New Customer</button>
              </div>
            </div>
            <div class="table-container">
              <table class="table table-striped">
                <tr>
                  <th>SN</th>
                  <th>Customer Name</th>
                  <th>Details</th>
                  <th>Status</th>
                  <th></th>
                </tr>

                <tr>
                  <td>01</td>
                  <td>Mr X</td>
                  <td>Polo shirt (Navy Blue), Size: XL, Phone: 01234567890, Address: 23, Tropical Akhand Tower (Level # 03), Sector # 11, Uttara, Dhaka - 1230</td>
                  <td>Active</td>
                  <td><img src="./images/three-dots-vertical.svg" alt=""></td>
                </tr>
                <tr>
                  <td>02</td>
                  <td>Mr X</td>
                  <td>Polo shirt (Navy Blue), Size: XL, Phone: 01234567890, Address: 23, Tropical Akhand Tower (Level # 03), Sector # 11, Uttara, Dhaka - 1230</td>

                  <td>Active</td>
                  <td><img src="./images/three-dots-vertical.svg" alt=""></td>
                </tr>
                <tr>
                  <td>03</td>
                 <td>Mr X</td>
                  <td>Polo shirt (Navy Blue), Size: XL, Phone: 01234567890, Address: 23, Tropical Akhand Tower (Level # 03), Sector # 11, Uttara, Dhaka - 1230</td>

                  <td>Active</td>
                  <td><img src="./images/three-dots-vertical.svg" alt=""></td>
                </tr>
                <tr>
                  <td>04</td>
                  <td>Mr X</td>
                  <td>Polo shirt (Navy Blue), Size: XL, Phone: 01234567890, Address: 23, Tropical Akhand Tower (Level # 03), Sector # 11, Uttara, Dhaka - 1230</td>

                  <td>Active</td>
                  <td><img src="./images/three-dots-vertical.svg" alt=""></td>
                </tr>
                <tr>
                  <td>05</td>
                  <td>Mr X</td>
                  <td>Polo shirt (Navy Blue), Size: XL, Phone: 01234567890, Address: 23, Tropical Akhand Tower (Level # 03), Sector # 11, Uttara, Dhaka - 1230</td>

                  <td>Active</td>
                  <td><img src="./images/three-dots-vertical.svg" alt=""></td>
                </tr>
                <tr>
                  <td>06</td>
                  <td>Mr X</td>
                  <td>Polo shirt (Navy Blue), Size: XL, Phone: 01234567890, Address: 23, Tropical Akhand Tower (Level # 03), Sector # 11, Uttara, Dhaka - 1230</td>

                  <td>Active</td>
                  <td><img src="./images/three-dots-vertical.svg" alt=""></td>
                </tr>
                <tr>
                  <td>07</td>
                  <td>Mr X</td>
                  <td>Polo shirt (Navy Blue), Size: XL, Phone: 01234567890, Address: 23, Tropical Akhand Tower (Level # 03), Sector # 11, Uttara, Dhaka - 1230</td>

                  <td>Active</td>
                  <td><img src="./images/three-dots-vertical.svg" alt=""></td>
                </tr>
                <tr>
                  <td>08</td>
                  <td>Mr X</td>
                  <td>Polo shirt (Navy Blue), Size: XL, Phone: 01234567890, Address: 23, Tropical Akhand Tower (Level # 03), Sector # 11, Uttara, Dhaka - 1230</td>

                  <td>Active</td>
                  <td><img src="./images/three-dots-vertical.svg" alt=""></td>
                </tr>
                <tr>
                  <td>09</td>
                  <td>Mr X</td>
                  <td>Polo shirt (Navy Blue), Size: XL, Phone: 01234567890, Address: 23, Tropical Akhand Tower (Level # 03), Sector # 11, Uttara, Dhaka - 1230</td>

                  <td>Active</td>
                  <td><img src="./images/three-dots-vertical.svg" alt=""></td>
                </tr>
              </table>
              <div class="table-bottom">
                <div class="table-bottom-right-side">
                  <label>Rows Per Page</label>
                  <span><select name="" id="">
                    <option value="">1</option>
                    <option value="">2</option>
                    <option value="">3</option>
                    <option value="">4</option>
                    <option value="">5</option>
                    <option value="">6</option>
                  </select></span>
                  <label for="">1-9 of 100</label>
                </div>

                <ul class="pagination">
                  <li class="page-item">
                    <a class="page-link previous" href="#">Prev</a>
                  </li>
                  <li class="page-item active"><a class="page-link" href="#">1</a></li>
                  <li class="page-item "><a class="page-link" href="#">2</a></li>
                  <li class="page-item"><a class="page-link" href="#">3</a></li>
                  <li class="page-item"><a class="page-link" href="#">...</a></li>
                  <li class="page-item"><a class="page-link" href="#">10</a></li>
                  <li class="page-item">
                    <a class="page-link next" href="#">Next</a>
                  </li>
                </ul>
              </div>
            </div>
          </section>
        </main>
      </div>
    </div>
  </body>
</template>

<script>
import sideBar from '@/components/layouts/sidebars/sideBar.vue'

export default{

  components:{
    sideBar
  },
  methods: {
        moveToSales(){
            this.$router.push('/dashboard');
        },
        moveToInventory(){
            this.$router.push('/inventory')
        },
        moveToCustomer(){
            this.$router.push('/customer')
        },
        moveToDispute(){
            this.$router.push('/dispute')
        },
        moveToReports(){
            this.$router.push('/reports')
      },
      moveTosystem(){
          this.$router.push('/system')
    }
}

}
</script>

<style>
@import url(https://befonts.com/avita-font.html);


@font-face {
	font-family: "Avita";
	src: url("./Avita-Typeface/Avita-Regular.otf");
	font-weight: normal;
	
}

body *{
    padding: 0;
    margin: 0;

}
.main-container{
    max-width: 100%;
}

aside{
    position: sticky;
    
     background-color: white;
    border: 1px solid  #E5E7EB;
    font-family: "Avita";
}

.sidebar-inner-wrap{
    height: 100vh;
}
aside nav ul li:hover,
aside nav ul li.selected {
    background-color: #002366
}

aside nav ul li a svg path{
    stroke:black;
}

aside nav ul li a{
    color: black;
}
aside nav ul li:hover a{
    color: #ffffff
}

aside nav ul li:hover a svg path{
    stroke: #ddd;
}

h1{
    display: inline;
}

.icon{
    
    background-color: white; 
    border: none;
    position:absolute;
    right: -15px;
    top: 13px;
}   

.nav-main{
    /* height: 896px; */
    padding-top: 8px;
    padding-left: 16px;
}

ul{
    list-style-type: none;
    padding: 0px !important;

}
li{
    border-radius: 8px;
    padding-top: 12px;
    padding-bottom: 12px;
    
}
li a, .settings a{
    color: black;
    text-decoration: none;
}

.settings{
    bottom: 10px;
    position: absolute;
}
li a, h1, .settings{
    padding-left: 16px;
}

li a img, .settings a img{
    padding-right: 8px;
}


main{
    padding-left: 0 !important;
    margin-left: 0 !important;
    display: flex;
    flex-direction: column;
}

main .top{
    background-color: white;
    
}

main .top span{
    float: right;
    padding: 16px;
}

.dropdown-toggle {
    background-color: white;
    border: none;
    position: relative;
}

.user-dropdown {
    background-color: #fff;
    border-radius: 10px;
    padding: 15px 0;
    box-shadow: 0px 3px 5px 1px #ddd;
    width: 200px;
    position: absolute;
    top: 100%;
    right: 0;
    text-align: left;
    display: none;
}
.dropdown-toggle:hover .user-dropdown {
    display: block;
}
.user-dropdown ul li a,
.user-dropdown h3 {
    font-size: 14px;
    font-weight: normal;
}
.user-dropdown ul li,
.user-dropdown h3 {
    padding: 5px 15px;
}
.user-dropdown ul li:hover {
    background-color: #ddd;
    border-radius: 0;
}
.user-dropdown .user-info-links {
    padding-bottom: 15px !important;
    border-bottom: 1px solid #ddd;
}
.settings-icon {
    margin-bottom: 0;
}

main {
    background-color: #F5F6FA;
}

.right-side-content-area{
    overflow-y: scroll; 
    max-height: calc(100vh - 100px);   
    margin: 20px;
    padding: 15px;
    background-color: white;
    border-radius: 24px;
    font-family: 'Figtree';
}

input{
    font-family: FontAwesome;
}

::placeholder{
    /* color: #F04A00; */
    font-family: FontAwesome;
}

.table-top{
    padding: 10px;
    display: flex;
    justify-content: space-between;
}
.table-top h3{
    padding: 12px 24px 12px 0px;
}
.table-top input{
    padding: 12px 24px 12px 24px;
    border: 1px solid;
    border-color: #E5E7EB;
    border-radius: 8px;
}

.table-top button{
    padding: 12px 24px 12px 24px;
    background-color: #F04A00;
    color: white;
    border: 0px;
    border-radius: 8px;
}

.table-bottom{
    display: flex;
    justify-content: space-between;
}

.table-bottom-right-side{
    padding-top: 10px;
    padding-bottom: 10px;
}

.pagination > li > a{
    color: black;
}
.pagination .previous::before{
    padding-right: 8px;
    content: '<';
    color: #F04A00;
}

.pagination .next::after{
    padding-left: 8px;
    content: '>';
    color: #F04A00; 
}

.pagination .next{
    color: #F04A00; 
}

.pagination .active a{
    background-color: #F04A00;
    border: none;
}

</style>