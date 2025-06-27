import FontAwesome from '@expo/vector-icons/FontAwesome';
import FontAwesome5 from '@expo/vector-icons/FontAwesome5';
import Ionicons from '@expo/vector-icons/Ionicons';

import { Tabs } from 'expo-router';

export default function TabLayout() {
  return (
    <Tabs screenOptions={{ headerShown: false, tabBarActiveTintColor: 'blue', tabBarInactiveTintColor: 'black',
      tabBarLabelStyle: {
        fontSize: 18,
        fontFamily: 'Roboto',
        fontWeight: 300,
      },
    }}>
      <Tabs.Screen
        name="ordering"
        options={{
          title: 'Pre-Order',
          tabBarIcon: ({ color }) => <Ionicons size={28} name="beer-outline" color={color} />,
        }}
      />
      <Tabs.Screen
        name="index"
        options={{
          title: 'Home',
          tabBarIcon: ({ color }) => <FontAwesome size={28} name="home" color={color} />,
        }}
      />
      <Tabs.Screen
        name="specials"
        options={{
          title: 'Specials',
          tabBarIcon: ({ color }) => <FontAwesome5 size={25} name="search-dollar" color={color} />,
        }}
      />
    </Tabs>
  );
}