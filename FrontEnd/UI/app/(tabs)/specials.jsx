import { View, Text, StyleSheet, Dimensions } from 'react-native';
import PagerView from 'react-native-pager-view';

const DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

export default function SpecialsTab() {
  const screenWidth = Dimensions.get('window').width;

  return (
    <PagerView style={styles.pagerView} initialPage={5}> {/* 5 = Friday */}
      {DAYS.map((day, index) => (
        <View key={index} style={styles.page}>
          {/* Custom header for each day */}
          <View style={styles.header}>
            <Text style={styles.headerText}>{day}</Text>
          </View>

          {/* Unique content for each day */}
          <View style={styles.content}>
            <Text>Specials for {day}</Text>
          </View>
        </View>
      ))}
    </PagerView>
  );
}

const styles = StyleSheet.create({
  pagerView: {
    flex: 1,
  },
  page: {
    flex: 1,
  },
  header: {
    backgroundColor: '#f2f2f2',
    paddingTop: 50, // for iPhone notch
    paddingBottom: 16,
    paddingHorizontal: 20,
    borderBottomWidth: 1,
    borderBottomColor: '#ccc',
  },
  headerText: {
    fontSize: 24,
    fontWeight: 'bold',
  },
  content: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});