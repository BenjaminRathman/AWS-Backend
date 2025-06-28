import React, { useRef, useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  Pressable,
  ScrollView,
  Image,
  Animated,
} from 'react-native';
import { useRouter } from 'expo-router';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { FontAwesome5 } from '@expo/vector-icons';

const images = [
  require('../assets/images/barlogos/blacktellus360transparent.png'),
  require('../assets/images/barlogos/tellus360.jpg'),
  require('../assets/images/barlogos/tellus360.jpg'),
  require('../assets/images/barlogos/tellus360.jpg'),
  require('../assets/images/barlogos/tellus360.jpg'),
];

const imageSizes = [
  { width: 140, height: 140 },
  { width: 140, height: 140 },
  { width: 140, height: 140 },
  { width: 140, height: 140 },
  { width: 140, height: 140 },
];

const rectangleTexts = [
  'Tellus 360',
  'Bar 2',
  'Bar 3',
  'Bar 4',
  'Bar 5',
];

const customBoxTexts = [
  'Custom info for Tellus 360',
  'Details about Bar 2 here',
  'Info for Bar 3 goes here',
  'More about Bar 4',
  'Description for Bar 5',
];

export default function Tab() {
  const router = useRouter();
  const insets = useSafeAreaInsets();

  return (
    <View style={styles.container}>
      {/* Header */}
      <View style={[styles.header, { paddingTop: insets.top + 10 }]}>
        <Pressable onPress={() => {}} style={styles.titleWrapper}>
          <Text style={styles.title}>Welcome!</Text>
        </Pressable>
        <Pressable onPress={() => router.push('/profile')} style={styles.iconWrapper}>
          <FontAwesome5 name="user-circle" size={30} color="#007AFF" />
        </Pressable>
      </View>

      {/* Scrollable Main Content */}
      <ScrollView contentContainerStyle={styles.scrollContent}>
        {images.map((imageSrc, index) => (
          <RectangleItem
            key={index}
            barId={['tellus360', 'bar2', 'bar3', 'bar4', 'bar5'][index]}
            imageSrc={imageSrc}
            imageSize={imageSizes[index]}
            text={rectangleTexts[index]}
            customBoxText={customBoxTexts[index]}
          />
        ))}
      </ScrollView>
    </View>
  );
}

function RectangleItem({
  barId,
  imageSrc,
  imageSize,
  text,
  customBoxText,
  customBoxWidth = 200,
  customBoxHeight = 180,
  customBoxBackground = '#e0e0e0',
}) {
  const slideAnim = useRef(new Animated.Value(0)).current;
  const boxOpacityAnim = useRef(new Animated.Value(0)).current;
  const [isRevealed, setIsRevealed] = useState(false);
  const router = useRouter();

  const handlePress = () => {
    if (!isRevealed) {
      // First press: slide and reveal text box
      Animated.timing(slideAnim, {
        toValue: 1,
        duration: 500,
        useNativeDriver: false,
      }).start(() => {
        setIsRevealed(true);
        Animated.timing(boxOpacityAnim, {
          toValue: 1,
          duration: 300,
          useNativeDriver: false,
        }).start();
      });
    } else {
      // Always allow navigation
      router.push(`/bars/${barId}`);
    }
  };

  const imageTranslate = slideAnim.interpolate({
    inputRange: [0, 1],
    outputRange: [0, 215],
  });

  const textOpacity = slideAnim.interpolate({
    inputRange: [0, 0.19],
    outputRange: [1, 0],
    extrapolate: 'clamp',
  });

  return (
    <Pressable
      onPress={handlePress}
      style={[styles.rectangle, { width: '105%', height: 200, paddingHorizontal: 5 }]}
    >
      {/* Revealed Text Box */}
      {isRevealed && (
        <Animated.View
          style={[
            styles.customBox,
            {
              opacity: boxOpacityAnim,
              width: customBoxWidth,
              height: customBoxHeight,
              backgroundColor: customBoxBackground,
              position: 'absolute',
              left: 5,
              top: '50%',
              transform: [{ translateY: -(customBoxHeight / 2) }],
              justifyContent: 'center',
              paddingHorizontal: 12,
            },
          ]}
        >
          <Text style={styles.customBoxText}>{customBoxText}</Text>
        </Animated.View>
      )}

      {/* Sliding Image */}
      <Animated.View style={{ transform: [{ translateX: imageTranslate }] }}>
        <Image
          source={imageSrc}
          style={{
            width: imageSize.width,
            height: imageSize.height,
            resizeMode: 'contain',
          }}
        />
      </Animated.View>

      {/* Text (fades out as image slides) */}
      <View style={styles.contentArea}>
        <Animated.Text style={[styles.rectangleText, { opacity: textOpacity }]}>
          {text}
        </Animated.Text>
      </View>
    </Pressable>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#333333' },
  header: {
    height: 80,
    paddingHorizontal: 20,
    justifyContent: 'center',
    position: 'relative',
    backgroundColor: '#333333',
    borderBottomColor: '#ccc',
    borderBottomWidth: 0,
    marginTop: 40,
  },
  titleWrapper: {
    position: 'absolute',
    left: 0,
    right: 0,
    alignItems: 'center',
  },
  title: { fontSize: 20, fontWeight: 'bold', color: '#ffffff' },
  iconWrapper: {
    position: 'absolute',
    left: 0,
    top: 5,
    bottom: 0,
    justifyContent: 'center',
    paddingLeft: 25,
  },
  scrollContent: {
    paddingTop: 25,
    paddingHorizontal: 20,
    paddingBottom: 80,
    alignItems: 'center',
    gap: 15,
  },
  rectangle: {
    flexDirection: 'row',
    borderRadius: 8,
    backgroundColor: '#fff',
    overflow: 'hidden',
    elevation: 3,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.15,
    shadowRadius: 4,
    alignItems: 'center',
    position: 'relative',
  },
  contentArea: { flex: 1, padding: 12, justifyContent: 'center' },
  rectangleText: { fontSize: 35, fontWeight: '500', color: '#333' },
  customBox: {
    padding: 12,
    backgroundColor: '#e0e0e0',
    borderRadius: 8,
  },
  customBoxText: {
    fontSize: 18,
    color: '#555',
  },
});
