function isPalindrome(x: number): boolean {
    const numberString = x.toString();
    const reversedString = numberString.split('').reverse().join('');
    return numberString === reversedString;
};