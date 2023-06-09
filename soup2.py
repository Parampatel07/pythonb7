from bs4 import BeautifulSoup
my_html='''
<!doctype html>
<html lang="zxx">
<head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <link rel="stylesheet" href="theme/assets/css/bootstrap.min.css">
     <link rel="stylesheet" href="theme/assets/css/owl.carousel.min.css">
     <link rel="stylesheet" href="theme/assets/css/owl.theme.default.min.css">
     <link rel="stylesheet" href="theme/assets/fonts/flaticon.css">
     <link rel="stylesheet" href="theme/assets/css/boxicons.min.css">
     <link rel="stylesheet" href="theme/assets/css/animate.min.css">
     <link rel="stylesheet" href="theme/assets/css/magnific-popup.css">
     <link rel="stylesheet" href="theme/assets/css/meanmenu.css">
     <link rel="stylesheet" href="theme/assets/css/nice-select.min.css">
     <link rel="stylesheet" href="theme/assets/css/style.css">
     <link rel="stylesheet" href="theme/assets/css/responsive.css">
     <link rel="stylesheet" href="theme/assets/css/theme-dark.css">
     <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
     <!-- Fancybox CSS -->
     <title>Dholera Site</title>
     <!-- <link rel="icon" type="image/png" href="theme/assets/img/favicon.png"> --><link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
<style>
     p {
          font-family: 'Montserrat', sans-serif;
     }

     .project-text {
          font-size: 1.1rem;
     }

     .key_features_background {
          background-image: url("images/background3.avif");
     }
</style>
</head>
<body>
     <div class="preloader">
     <div class="d-table">
          <div class="d-table-cell">
               <div class="spinner">
                    <div class="circle1"></div>
                    <div class="circle2"></div>
                    <div class="circle3"></div>
               </div>
          </div>
     </div>
</div>
<div class="navbar-area">
     <div class="mobile-nav">
          <a href="index.html" class="logo">
               <img src="theme/assets/img/logos/footer-logo.png" class="logo-one" alt="Logo">
               <img src="theme/assets/img/logos/logo-4.png" class="logo-two" alt="Logo">
          </a>
     </div>
     <div class="top-nav main-nav">
          <div class="container-fluid">
               <nav class="container-max navbar navbar-expand-md navbar-light ">
                    <!-- <a class="navbar-brand" href="index.html">
                         <img src="images/mylogo2.png"  class="logo-one img-fluid" alt="Logo">
                         <img src="images/mylogo2.png"  class="logo-two img-fluid" alt="Logo">
                    </a> -->
                    <div class="collapse navbar-collapse mean-menu" id="navbarSupportedContent">
                         <ul class="navbar-nav m-auto ">
                              <!-- <li class="nav-item"> -->
                              <!-- <a href="#" class="nav-link active">
                                             Home
                                             <i class='bx bx-chevron-down'></i>
                                        </a> -->
                              <!-- <ul class="dropdown-menu">
                                             <li class="nav-item">
                                                  <a href="index.html" class="nav-link">
                                                       Home One
                                                  </a>
                                             </li>
                                             <li class="nav-item">
                                                  <a href="index-2.html" class="nav-link active">
                                                       Home Two
                                                  </a>
                                             </li>
                                             <li class="nav-item">
                                                  <a href="index-3.html" class="nav-link">
                                                       Home Three
                                                  </a>
                                             </li>
                                        </ul> -->
                              <!-- </li> -->
                              <li class="nav-item">
                                   <a href="index.php" class="nav-link">
                                        Home
                                   </a>
                              </li>
                              <li class="nav-item">
                                   <a href="features.php" class="nav-link">
                                        Features
                                   </a>
                              </li>
                              <li class="nav-item">
                                   <a href="mega_project.php" class="nav-link">
                                        Mega Project
                                   </a>
                              </li>
                              <li class="nav-item">
                                   <a href="investing.php" class="nav-link">
                                        Benefits
                                   </a>
                              </li>
                              <li class="nav-item">
                                   <a href="overview.php" class="nav-link">
                                        Overview
                                   </a>
                              </li>
                              <li class="nav-item">
                                   <a href="gallery.php" class="nav-link">
                                        Gallery
                                   </a>
                              </li>
                              <li class="nav-item">
                                   <a href="contactus.php" class="nav-link">
                                        Contact Us
                                   </a>
                              </li>
                         </ul>
                         <div id="google_translate_element"></div>
                    </div>
               </nav>
          </div>
     </div>
</div>     <section class="mb-5">
          <div class="home-slider-area">
               <div class="container-fluid m-0 p-0">
                    <div class="home-slider owl-carousel owl-theme">
                         <div class="slider-item " style="background-color: #ECDDB4;">
                              <div class="row align-items-center">
                                   <div class="col-lg-5 col-xxl-6">
                                        <div class="home-slider-content">
                                             <h1>India first Planned Smart City</h1>
                                        </div>
                                   </div>
                                   <div class="col-lg-7 col-xxl-6 pr-0">
                                        <div class="home-slider-img">
                                             <img src="images/slider1_2.jpg" class="img-fluid" style="height:539px;width:100%;" alt="Images">
                                        </div>
                                   </div>
                              </div>
                         </div>
                         <div class="slider-item" style="background-color: #A6D0DD;">
                              <div class="row align-items-center">
                                   <div class="col-lg-5 col-xxl-6">
                                        <div class="home-slider-content">
                                             <h1>Dholera will be better developed then Delhi</b></h1>
                                        </div>
                                   </div>
                                   <div class="col-lg-7 col-xxl-6 pr-0">
                                        <div class="home-slider-img">
                                             <img src="images/slider2.jpg" class="img-fluid" style="height:539px;width:100%;" alt="Images">
                                        </div>
                                   </div>
                              </div>
                         </div>
                         <div class="slider-item" style="background-color: #E3D6CB;">
                              <div class="row align-items-center">
                                   <div class="col-lg-5 col-xxl-6">
                                        <div class="home-slider-content">
                                             <h1>Excellent Road and Rail connectivity</b></h1>
                                        </div>
                                   </div>
                                   <div class="col-lg-7 col-xxl-6 pr-0">
                                        <div class="home-slider-img">
                                             <img src="images/slider3.jpg" class="img-fluid" style="height:539px;width:100%;" alt="Images">
                                        </div>
                                   </div>
                              </div>
                         </div>
                         <div class="slider-item" style="background-color: #C7E9B0;">
                              <div class="row align-items-center">
                                   <div class="col-lg-5 col-xxl-6">
                                        <div class="home-slider-content">
                                             <h1>Find Your Lovely & <b>Comfort Home</b></h1>
                                        </div>
                                   </div>
                                   <div class="col-lg-7 col-xxl-6 pr-0">
                                        <div class="home-slider-img">
                                             <img src="images/slider4.jpg" class="img-fluid" style="height:539px;width:100%;" alt="Images">
                                        </div>
                                   </div>
                              </div>
                         </div>
                    </div>
               </div>
          </div>
     </section>
     <section style="margin-top: 100px;" >
          <div class="container">
               <h1 align="center" class="mb-4">
                    <a align="center" href="mega_project.php" style="color:#234467;">
                         Know more about Dholera Smart city
                    </a>
               </h1>
               <div class="row">
                    <div class="col-lg-6 col-md-6 mb-5" data-aos="fade-right" data-aos-duration="1000">
                         <div class="service-item " style="height:100%;">
                              <i class="flaticon-bankrupt"></i>
                              <a>
                                   <h3>Dholera SIR- India's PM Narendra Modi's Dream Project</h3>
                              </a>
                              <p>
                                   The vision of Dolera SIR is "The Development Plan, taking into account the DMIC objectives and goals, should focus towards creating and enabling environment to protect local industries, enhance investment climate, improve quality of life, upgrade human skills, create world class infrastructure and attract global investment".

                                   Project goals are to double the employement potential, triple industrial output and quadruple exports from the region in next five years.
                                   Moreover the schemes comprises all modern amenities & excellent infrastructure design with Prime lowest Price & EMI option with flexible time duration.
                              </p>
                         </div>
                    </div>
                    <div class="col-lg-6 col-md-6 mb-5" data-aos="fade-left" data-aos-duration="1000">
                         <div class="service-item" style="height:100%;">
                              <i class="flaticon-value"></i>
                              <a>
                                   <h3>Dholera International Airport</h3>
                              </a>
                              <p class="mb-4">
                              <ul>
                                   <li>
                                        New International Airport on the Northern tip, 1 Kms away of SIR
                                   </li>
                                   <li>
                                        9200 hectors Government land reserved by State Govt of Gujarat
                                   </li>
                                   <li>
                                        DPR under preparation by Airport Authority of India
                                   </li>
                                   <li>
                                        Site Suitability estabilished by Airport Authority of India
                                   </li>
                                   <li>
                                        SPV has been formed by GoG Cargo as well as passenger Airport facility will be available
                                   </li>
                                   <li>
                                        State has included the development of an International Airport in the list of “Early Bird Projects” in consultation with Department of Industrial Promotion and Policy
                                   </li>
                              </ul>
                              </p>
                         </div>
                    </div>
                    <div class="col-lg-6 col-md-6 mb-5" data-aos="fade-right" data-aos-duration="1000">
                         <div class="service-item " style="height:100%;">
                              <i class="flaticon-bankrupt"></i>
                              <a>
                                   <h3>Dholera Metro Train (MRTS)</h3>
                              </a>
                              <p>
                                   In Metro rail the distance between Gandhinagar-Ahmedabad-Dholera Smart City is to be covered in two trenches from Gandhinagar to Ahmedabad and from Ahmedabad to Dholera. It is about 100 kms and is proposed as elevated metro. This will provide faster movement and even otherwise important for new international air port. The metro is also approved under DMIC master plan by the central govt.

                                   In one of the meetings with secretary DIPP, during his visit to Gandhinagar it was thought of high speed rail corridor on this route. It is related to pre- feasibility study being carried out by the ministry of railways for Pune-Mumbai-Ahmedbad high speed rail corridor.

                              </p>
                         </div>
                    </div>
                    <div class="col-lg-6 col-md-6 mb-5" data-aos="fade-left" data-aos-duration="1000">
                         <div class="service-item" style="height:100%;">
                              <i class="flaticon-value"></i>
                              <a>
                                   <h3>Central Spine Road (Sh6)</h3>
                              </a>
                              <p class="mb-4">
                                   The Gujarat State Road Development Corporation Limited (GSRDC) is developing an access controlled expressway Between Ahmedabad & DSIR to Serve as a Central Spine Road for Dholera SIR. he proposed road would serve as central spine for Ahmedabad-Dholera SIR. It is decided that initially the road will be four lane with six lane structure. It could be access controlled.

                                   The road is supposed to connect the Ahmedabad city on one hand and Dholera Smart City and Bhavnagar ports on the other side. It is envisaged that the new industry cluster to be developed along the spine would considerably benefit with central linkage.
                              </p>
                         </div>
                    </div>
               </div>
          </div>
     </section>
     <section>
          <div class="project-area key_features_background">
               <div class="container">
                    <div class="row">
                         <div class="col-6"></div>
                         <div class="col-lg-6" data-aos="fade-up-right" data-aos-duration="1000">
                              <div class="project-card">
                                   <!-- <span>NEW PROJECT IN PROGRESS</span> -->
                                   <a href="features.php">
                                        <h2>Key feature of dholera smart city</h2>
                                   </a>
                                   <ul>
                                        <li>
                                             <p class="project-text">Dream Project of Mr. Narendra Modi envisaged when he was the Chief Minister of Gujarat.</p>
                                        </li>
                                        <li>
                                             <p class="project-text">To be developed 2 times the size of Delhi and Six times that of ShanghaiF</p>
                                        </li>
                                        <li>
                                             <p class="project-text">Rated by Forbes as one of its kind cities in India and one amongst Top 12 fastest growing cities in the world</p>
                                        </li>
                                        <li>
                                             <p class="project-text">Excellent connectivity through rail, road, express highway, international airport, metro and port which collectively links the city on both national and global front</p>
                                        </li>
                                        <li>
                                             <p class="project-text">First choice for smart investors owing to its strategic location, current prices and thrust from the government</p>
                                        </li>
                                        <li>
                                             <p class="project-text">First choice for smart investors owing to its strategic location, current prices and thrust from the government</p>
                                        </li>
                                        <li>
                                             <p class="project-text">Sea Pipavav Port in the vicinity - Best for doing business / trades</p>
                                        </li>
                                        <li>
                                             <p class="project-text">Reshaping of irregular shaped plot is completed in FP (Final Plot). </p>
                                        </li>
                                   </ul>
                              </div>
                         </div>
                    </div>
               </div>
          </div>
     </section>
     <div class="container">
          <section>
               <div class="property-area pt-100 pb-70">
                    <div class="container">
                         <div class="row align-items-center">
                              <div class="col-lg-12">
                                   <div class="property-item">
                                        <div class="service-area p-5" data-aos="fade-right" data-aos-duration="1000">
                                             <div class="section-title">
                                                  <h2>
                                                       <a href="investing.php" data-aos="zoom-in" data-aos-duration="1400">
                                                            Benefit of investing in dholera
                                                       </a>
                                                  </h2>
                                                  <p>
                                                       Dholera SIR (Special Investment Region) is a rapidly developing city located in the state of Gujarat, India. As the first smart city of India, Dholera SIR is a promising destination for investors looking to invest in real estate. Investing in Dholera SIR offers a range of benefits, including access to world-class infrastructure, a thriving business environment, and significant growth potential. In this fast-growing city, investors can enjoy attractive returns on their investment, as well as a high standard of living and numerous amenities. With its strategic location, modern infrastructure, and investor-friendly policies, Dholera SIR is quickly becoming one of the most sought-after investment destinations in India.
                                                  </p>
                                             </div>
                                             <div class="container mt-4">
                                                  <div class="row">
                                                       <div class="col-lg-3 col-sm-6" data-aos="zoom-out" data-aos-duration="1500">
                                                            <div class="service-card service-card-bg p-3">
                                                                 <i class="fa-solid fa-indian-rupee-sign"></i>
                                                                 <a>
                                                                      <h3>Price Appreciation</h3>
                                                                 </a>
                                                            </div>
                                                       </div>
                                                       <div class="col-lg-3 col-sm-6" data-aos="zoom-out" data-aos-duration="1700">
                                                            <div class="service-card service-card-bg p-3">
                                                                 <i class="fa-solid fa-building-columns"></i>
                                                                 <a>
                                                                      <h3>Rental Income</h3>
                                                                 </a>
                                                            </div>
                                                       </div>
                                                       <div class="col-lg-3 col-sm-6" data-aos="zoom-out" data-aos-duration="1900">
                                                            <div class="service-card service-card-bg p-3">
                                                                 <i class="fa-solid fa-user-tie"></i>
                                                                 <a>
                                                                      <h3>Job/Bussniess Opportunities</h3>
                                                                 </a>
                                                            </div>
                                                       </div>
                                                       <div class="col-lg-3 col-sm-6" data-aos="zoom-out" data-aos-duration="2100">
                                                            <div class="service-card service-card-bg p-3">
                                                                 <i class="fa-solid fa-house-user"></i>
                                                                 <a>
                                                                      <h3>High Quality Life</h3>
                                                                 </a>
                                                            </div>
                                                       </div>
                                                  </div>
                                             </div>
                                        </div>
                                   </div>
                              </div>
                         </div>
                    </div>
               </div>
          </section>
     </div>
     <section>
          <div class="testimonial-area ptb-100">
               <div class="container">
                    <h2 align="center" data-aos="zoom-out" data-aos-duration="2000">
                         Key people statements abot dholera smart city
                    </h2>
                    <div class="testimonial-slider owl-carousel owl-theme">
                         <div class="testimonial-item">
                              <h3>Shree Narendra Modi (Hon. P.M.)</h3>
                              <p>
                                   Dholera will be developed better than Delhi and six times bigger than Shanghai
                              </p>
                         </div>
                         <div class="testimonial-item">
                              <h3>Shree Nitin Gadkari (Hon. Minister for Road Transport & Highways)</h3>
                              <p>
                                   Bhavnagar - Dholera - Khambhat to be developed as National highway
                              </p>
                         </div>
                         <div class="testimonial-item">
                              <h3>Rajnath Singh (Hon. Defence Minister)</h3>
                              <p>
                                   After Baroda, there will be 2nd Aircraft unit will be created in dholera
                              </p>
                         </div>
                    </div>
               </div>
          </div>
     </section>
          <div class="footer-bottom">
          <div class="container">
               <div class="bottom-text">
                    <p>
                         Copyright © <script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script>
                         <script>
                              document.write(new Date().getFullYear())
                         </script>
                         <a href="https://theeasylearnacademy.com/" target="_blank">The Easylearn Academy</a>
                    </p>
               </div>
          </div>
     </div>
     </footer>
     <script src="theme/assets/js/jquery.min.js"></script>
     <script src="theme/assets/js/bootstrap.bundle.min.js"></script>
     <script src="theme/assets/js/owl.carousel.min.js"></script>
     <script src="theme/assets/js/meanmenu.js"></script>
     <script src="theme/assets/js/jquery.magnific-popup.min.js"></script>
     <script src="theme/assets/js/wow.min.js"></script>
     <script src="theme/assets/js/jquery.nice-select.min.js"></script>
     <script src="theme/assets/js/jquery.ajaxchimp.min.js"></script>
     <script src="theme/assets/js/form-validator.min.js"></script>
     <script src="theme/assets/js/contact-form-script.js"></script>
     <script src="theme/assets/js/custom.js"></script>
     <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
     <script>
          AOS.init(4000);
     </script>
     <script type="text/javascript">
          function googleTranslateElementInit() {
               new google.translate.TranslateElement({
                    pageLanguage: 'en',
                    layout: google.translate.TranslateElement.InlineLayout.SIMPLE
               }, 'google_translate_element');
          }
     </script>
     <script src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
     </script></body>
</html>
'''
formated_html = BeautifulSoup(my_html,'html.parser')
print(formated_html.prettify())

print(formated_html.p)
print(formated_html.p.string)
print(formated_html.find_all('p'))

