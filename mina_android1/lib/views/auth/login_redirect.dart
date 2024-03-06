import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:mina_fixed1/common/app_style.dart';
import 'package:mina_fixed1/common/custom_button.dart';
import 'package:mina_fixed1/common/custom_container.dart';
import 'package:mina_fixed1/common/reusable_text.dart';
import 'package:mina_fixed1/constants/constants.dart';
import 'package:mina_fixed1/views/auth/login_page.dart';
import 'package:get/get.dart';
import 'package:lottie/lottie.dart';

class LoginRedirect extends StatelessWidget {
  const LoginRedirect({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: kPrimary,
      appBar: AppBar(
        backgroundColor: kLightWhite,
        elevation: 0.3,
        title: ReusableText(
            text: "Please login to access this page",
            style: appStyle(12, kDark, FontWeight.w500)),
      ),
      body: SafeArea(
        child: CustomContainer(
            containerContent: Column(
          children: [
            Container(
              width: width,
              height: height / 2,
              color: Colors.white,
              child: LottieBuilder.asset(
                "assets/anime/delivery.json",
                width: width,
                height: height / 2,
              ),
            ),
            CustomButton(
              text: "L O G I N",
              onTap: () {
                Get.to(() => const LoginPage(),
                    transition: Transition.cupertino,
                    duration: const Duration(milliseconds: 900));
              },
              btnHeight: 40.h,
              btnWidth: width - 20,
            )
          ],
        )),
      ),
    );
  }
}
