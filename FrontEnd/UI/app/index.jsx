function RectangleItem({ imageSrc, imageSize, text }) {
  const slideAnim = useRef(new Animated.Value(0)).current;
  const [textVisible, setTextVisible] = useState(true);

  const handlePress = () => {
    Animated.timing(slideAnim, {
      toValue: 1,
      duration: 500,
      useNativeDriver: false,
    }).start(() => {
      // Hide the text only after the animation completes
      setTextVisible(false);
    });
  };

  const imageTranslate = slideAnim.interpolate({
    inputRange: [0, 1],
    outputRange: [0, 215], // Slide right distance
  });

  return (
    <Pressable
      onPress={handlePress}
      style={[
        styles.rectangle,
        { width: '105%', height: 200, paddingHorizontal: 5 },
      ]}
    >
      {/* Text underneath */}
      <View style={styles.contentArea}>
        {textVisible && <Text style={styles.rectangleText}>{text}</Text>}
      </View>

      {/* Image on top that slides over */}
      <Animated.View
        style={[
          {
            position: 'absolute',
            left: 5,
            top: 30,
            transform: [{ translateX: imageTranslate }],
            zIndex: 1,
          },
        ]}
      >
        <Image
          source={imageSrc}
          style={{
            width: imageSize.width,
            height: imageSize.height,
            resizeMode: 'contain',
          }}
        />
      </Animated.View>
    </Pressable>
  );
}
