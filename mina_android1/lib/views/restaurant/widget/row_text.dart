import 'package:flutter/material.dart';
import 'package:mina_fixed1/common/app_style.dart';
import 'package:mina_fixed1/common/reusable_text.dart';
import 'package:mina_fixed1/constants/constants.dart';

class RowText extends StatelessWidget {
  const RowText({
    super.key,
    required this.first,
    required this.second,
  });

  final String first;
  final String second;

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        ReusableText(text: first, style: appStyle(10, kGray, FontWeight.w500)),
        ReusableText(text: second, style: appStyle(10, kGray, FontWeight.w500))
      ],
    );
  }
}
